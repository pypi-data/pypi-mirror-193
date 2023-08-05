'''
[![NPM version](https://badge.fury.io/js/cdk-efs-assets.svg)](https://badge.fury.io/js/cdk-efs-assets)
[![PyPI version](https://badge.fury.io/py/cdk-efs-assets.svg)](https://badge.fury.io/py/cdk-efs-assets)
![Release](https://github.com/pahud/cdk-efs-assets/workflows/Release/badge.svg)

# cdk-efs-assets

CDK construct library to populate Amazon EFS assets from Github or S3. If the source is S3, the construct also optionally supports updating the contents in EFS if a new zip file is uploaded to S3.

## Install

TypeScript/JavaScript:

```bash
npm i cdk-efs-assets
```

## SyncedAccessPoint

The main construct that is used to provide this EFS sync functionality is `SyncedAccessPoint`. This extends the standard EFS `AccessPoint` construct, and takes an additional `SyncSource` constructor property which defines the source to sync assets from. The `SyncedAccessPoint` instance can be used anywhere an `AccessPoint` can be used. For example, to specify a volume in a Task Definition:

```python
const taskDefinition = new ecs.FargateTaskDefinition(this, 'TaskDefinition', {
  ...
  volumes: [
    {
      name: 'efs-storage',
      efsVolumeConfiguration: {
        fileSystemId: sharedFileSystem.fileSystemId,
        transitEncryption: 'ENABLED',
        authorizationConfig: {
          accessPointId: syncedAccessPoint.accessPointId
        }
      }
    },
  ]
});
```

## Sync Engine

This library supports both `AWS Fargate` and `AWS Lambda` as the sync engine. As AWS Lambda currently has know issue with Amazon EFS([#100](https://github.com/pahud/cdk-efs-assets/issues/100)), the default sync engine is `AWS Fargate`. You can opt in AWS Lambda with the `engine` construct property of `SyncedAccessPoint`.

## Sync Source

Use `GithubSyncSource` and `S3ArchiveSyncSource` construct classes to define your `syncSource` from Github
or Amazon S3 bucket. For example:

To define a public github repository as the `syncSource`:

```python
new SyncedAccessPoint(stack, 'EfsAccessPoint', {
  ...
  syncSource: new GithubSyncSource({
    vpc,
    repository: 'https://github.com/pahud/cdk-efs-assets.git',
  }),
});
```

To define a private github repository as the `syncSource`:

```python
new SyncedAccessPoint(stack, 'EfsAccessPoint', {
  ...
  syncSource: new GithubSyncSource({
    vpc,
    repository: 'https://github.com/pahud/private-repo.git',
    secret: {
      id: 'github',
      key: 'oauth_token',
    },
  }),
});
```

### `syncDirectoryPath`

By default, the synced EFS assets are placed into a directory corresponding to the type of the sync source. For example, the default behavior of the GitHub source is to place the copied files into a directory named the same as the repository name (for a repository specified as 'https://github.com/pahud/cdk-efs-assets.git', the directory name would be 'cdk-efs-assets'), while the default behavior of the S3 archive source is to place the copied files into a directory named the same as the zip file (for a zip file name of 'assets.zip', the directory name would be 'assets').

If you wish to override this default behavior, specify a value for the `syncDirectoryPath` property that is passed into the `SyncSource` call.

If you are using the `AccessPoint` in an ECS/Fargate Task Definition, you probably will want to override the value of `syncDirectoryPath` to '/'. This will place the file contents in the root directory of the Access Point. The reason for this is that when you create a volume that is referencing an EFS Access Point, you are not allowed to specify any path other than the root directory in the task definition configuration.

## How to use SyncedAccessPoint initialized with files provisioned from GitHub repository

This will sync assets from a GitHub repository to a directory (by default, the output directory is named after the repository name) in the EFS AccessPoint:

```python
import { SyncSource, SyncedAccessPoint } from 'cdk-efs-assets';

const app = new App();

const env = {
  region: process.env.CDK_DEFAULT_REGION ?? AWS_DEFAULT_REGION,
  account: process.env.CDK_DEFAULT_ACCOUNT,
};

const stack = new Stack(app, 'testing-stack', { env });

const vpc = ec2.Vpc.fromLookup(stack, 'Vpc', { isDefault: true })

const fileSystem = new efs.FileSystem(stack, 'Filesystem', {
  vpc,
  removalPolicy: RemovalPolicy.DESTROY,
})

const efsAccessPoint = new SyncedAccessPoint(stack, 'GithubAccessPoint', {
  vpc,
  fileSystem,
  path: '/demo-github',
  createAcl: {
    ownerGid: '1001',
    ownerUid: '1001',
    permissions: '0755',
  },
  posixUser: {
    uid: '1001',
    gid: '1001',
  },
  syncSource: new GithubSyncSource({
    vpc,
    repository: 'https://github.com/pahud/cdk-efs-assets.git',
  })
});
```

### Github private repository support

To clone a github private repository, you need to generate your github **PAT(Personal Access Token)** and store the token in **AWS Secrets Manager** secret.

For example, if your PAT is stored in the AWS Secret manager with the secret ID `github` and the key `oauth_token`, you can specify the `secret` property as the sample below. Under the covers the lambda function will format the full github repository uri with your **PAT** and successfully git clone the private repository to the efs filesystem.

Store your PAT into the AWS Secrets Manager with AWS CLI:

```sh
aws secretsmanager create-secret \
--name github \
--secret-string '{"oauth_token":"MYOAUTHTOKEN"}'
```

Configure the `secret` property to allow lambda to retrieve the **PAT** from the secret:

```python
new GithubSyncSource({
    vpc,
    repository: 'https://github.com/username/repo.git',
    secret: {
      id: 'github',
      key: 'oauth_token',
    },
})
```

## How to use SyncedAccessPoint initialized with files provisioned from zip file stored in S3

This will sync assets from a zip file stored in an S3 bucket to a directory (by default, the output directory is named after the zip file name) in the EFS AccessPoint:

```python
import { S3ArchiveSync } from 'cdk-efs-assets';

const app = new App();

const env = {
  region: process.env.CDK_DEFAULT_REGION ?? AWS_DEFAULT_REGION,
  account: process.env.CDK_DEFAULT_ACCOUNT,
};

const stack = new Stack(app, 'testing-stack', { env });

const vpc = ec2.Vpc.fromLookup(stack, 'Vpc', { isDefault: true })

const fileSystem = new efs.FileSystem(stack, 'Filesystem', {
  vpc,
  removalPolicy: RemovalPolicy.DESTROY,
})

const bucket = Bucket.fromBucketName(this, 'Bucket', 'demo-bucket');

const efsAccessPoint = new SyncedAccessPoint(stack, 'EfsAccessPoint', {
  vpc,
  fileSystem,
  path: '/demo-s3',
  createAcl: {
    ownerGid: '1001',
    ownerUid: '1001',
    permissions: '0755',
  },
  posixUser: {
    uid: '1001',
    gid: '1001',
  },
  syncSource: new S3ArchiveSyncSource({
    vpc,
    bucket,
    zipFilePath: 'folder/foo.zip',
  }),
});
```

### syncOnUpdate

If the `syncOnUpdate` property is set to `true` (defaults to `true`), then the specified zip file path will be monitored, and if a new object is uploaded to the path, then it will resync the data to EFS. Note that to use this functionality, you must have a CloudTrail Trail in your account that captures the desired S3 write data event.

This feature is only available with the `LAMBDA` sync engine.

*WARNING*: The contents of the extraction directory in the access point will be destroyed before extracting the zip file.

# `StatefulFargateNginx`

This library comes with `StatefulFargateNginx` construct which allows you to build an Amazon EFS-backed stateful
AWS Fargate service with its document root seeded from any github repository.

See this [tweet](https://twitter.com/pahudnet/status/1367792169063354371) for the demo.

Sample:

```python
new StatefulFargateNginx(this, 'NyanCat', {
  vpc,
  github: 'https://github.com/cristurm/nyan-cat.git',
});
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_ecs as _aws_cdk_aws_ecs_ceddda9d
import aws_cdk.aws_ecs_patterns as _aws_cdk_aws_ecs_patterns_ceddda9d
import aws_cdk.aws_efs as _aws_cdk_aws_efs_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


class EfsFargateSite(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-efs-assets.EfsFargateSite",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
        task: _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_point: 
        :param task: 
        :param vpc: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a20ce890668e81b5e889b725552e04817338b13b4a8d701527047b099d24c5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EfsFargateSiteProps(access_point=access_point, task=task, vpc=vpc)

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(
        self,
    ) -> _aws_cdk_aws_ecs_patterns_ceddda9d.ApplicationLoadBalancedFargateService:
        return typing.cast(_aws_cdk_aws_ecs_patterns_ceddda9d.ApplicationLoadBalancedFargateService, jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition:
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition, jsii.get(self, "task"))


@jsii.data_type(
    jsii_type="cdk-efs-assets.EfsFargateSiteProps",
    jsii_struct_bases=[],
    name_mapping={"access_point": "accessPoint", "task": "task", "vpc": "vpc"},
)
class EfsFargateSiteProps:
    def __init__(
        self,
        *,
        access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
        task: _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    ) -> None:
        '''
        :param access_point: 
        :param task: 
        :param vpc: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad14ca58a5088c5b480664cae28f48c52f45edbaa2494286fcfa0958682904e)
            check_type(argname="argument access_point", value=access_point, expected_type=type_hints["access_point"])
            check_type(argname="argument task", value=task, expected_type=type_hints["task"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_point": access_point,
            "task": task,
            "vpc": vpc,
        }

    @builtins.property
    def access_point(self) -> _aws_cdk_aws_efs_ceddda9d.AccessPoint:
        result = self._values.get("access_point")
        assert result is not None, "Required property 'access_point' is missing"
        return typing.cast(_aws_cdk_aws_efs_ceddda9d.AccessPoint, result)

    @builtins.property
    def task(self) -> _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition:
        result = self._values.get("task")
        assert result is not None, "Required property 'task' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition, result)

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EfsFargateSiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EfsFargateTask(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-efs-assets.EfsFargateTask",
):
    '''Represents the AWS Fargate task with EFS and secret manager support.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
        sync_container: typing.Union[_aws_cdk_aws_ecs_ceddda9d.ContainerDefinitionOptions, typing.Dict[builtins.str, typing.Any]],
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        efs_mount_target: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union["GithubSecret", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_point: 
        :param sync_container: 
        :param vpc: 
        :param efs_mount_target: EFS mount target in the container. Default: /mnt/efsmount
        :param secret: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea248b6c4413e2452dfed8d02ea535672572b6e000823ed4a98be4b443a24f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EfsFargateTaskProps(
            access_point=access_point,
            sync_container=sync_container,
            vpc=vpc,
            efs_mount_target=efs_mount_target,
            secret=secret,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> _aws_cdk_aws_ec2_ceddda9d.SecurityGroup:
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.SecurityGroup, jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition:
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition, jsii.get(self, "task"))


@jsii.data_type(
    jsii_type="cdk-efs-assets.EfsFargateTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_point": "accessPoint",
        "sync_container": "syncContainer",
        "vpc": "vpc",
        "efs_mount_target": "efsMountTarget",
        "secret": "secret",
    },
)
class EfsFargateTaskProps:
    def __init__(
        self,
        *,
        access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
        sync_container: typing.Union[_aws_cdk_aws_ecs_ceddda9d.ContainerDefinitionOptions, typing.Dict[builtins.str, typing.Any]],
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        efs_mount_target: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union["GithubSecret", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_point: 
        :param sync_container: 
        :param vpc: 
        :param efs_mount_target: EFS mount target in the container. Default: /mnt/efsmount
        :param secret: 
        '''
        if isinstance(sync_container, dict):
            sync_container = _aws_cdk_aws_ecs_ceddda9d.ContainerDefinitionOptions(**sync_container)
        if isinstance(secret, dict):
            secret = GithubSecret(**secret)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f197af0923d3303af0c30ff7435b02b6cf7fd5be713fc1b89d0d9e4793e0cb50)
            check_type(argname="argument access_point", value=access_point, expected_type=type_hints["access_point"])
            check_type(argname="argument sync_container", value=sync_container, expected_type=type_hints["sync_container"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument efs_mount_target", value=efs_mount_target, expected_type=type_hints["efs_mount_target"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_point": access_point,
            "sync_container": sync_container,
            "vpc": vpc,
        }
        if efs_mount_target is not None:
            self._values["efs_mount_target"] = efs_mount_target
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def access_point(self) -> _aws_cdk_aws_efs_ceddda9d.AccessPoint:
        result = self._values.get("access_point")
        assert result is not None, "Required property 'access_point' is missing"
        return typing.cast(_aws_cdk_aws_efs_ceddda9d.AccessPoint, result)

    @builtins.property
    def sync_container(self) -> _aws_cdk_aws_ecs_ceddda9d.ContainerDefinitionOptions:
        result = self._values.get("sync_container")
        assert result is not None, "Required property 'sync_container' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.ContainerDefinitionOptions, result)

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def efs_mount_target(self) -> typing.Optional[builtins.str]:
        '''EFS mount target in the container.

        :default: /mnt/efsmount
        '''
        result = self._values.get("efs_mount_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret(self) -> typing.Optional["GithubSecret"]:
        result = self._values.get("secret")
        return typing.cast(typing.Optional["GithubSecret"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EfsFargateTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-efs-assets.FargateTaskConfig",
    jsii_struct_bases=[],
    name_mapping={"security_group": "securityGroup", "task": "task"},
)
class FargateTaskConfig:
    def __init__(
        self,
        *,
        security_group: _aws_cdk_aws_ec2_ceddda9d.ISecurityGroup,
        task: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
    ) -> None:
        '''
        :param security_group: The security group of the fargate task.
        :param task: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93a49c6dadc8eec97c51e0ff9e68eb9f8bfad4923a6dfc282ac262c2d162e8b0)
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument task", value=task, expected_type=type_hints["task"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group": security_group,
            "task": task,
        }

    @builtins.property
    def security_group(self) -> _aws_cdk_aws_ec2_ceddda9d.ISecurityGroup:
        '''The security group of the fargate task.'''
        result = self._values.get("security_group")
        assert result is not None, "Required property 'security_group' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup, result)

    @builtins.property
    def task(self) -> _aws_cdk_aws_ecs_ceddda9d.TaskDefinition:
        result = self._values.get("task")
        assert result is not None, "Required property 'task' is missing"
        return typing.cast(_aws_cdk_aws_ecs_ceddda9d.TaskDefinition, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateTaskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-efs-assets.GithubSecret",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "key": "key"},
)
class GithubSecret:
    def __init__(self, *, id: builtins.str, key: builtins.str) -> None:
        '''
        :param id: The secret ID from AWS Secrets Manager.
        :param key: The key of the secret.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cac7dfb8948f0cafd529ea5ab43067c550dd6bc8a8b653dcbd78d388e2ce930b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "key": key,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''The secret ID from AWS Secrets Manager.'''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''The key of the secret.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StatefulFargateNginx(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-efs-assets.StatefulFargateNginx",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        efs_file_system: typing.Optional[_aws_cdk_aws_efs_ceddda9d.IFileSystem] = None,
        github: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param efs_file_system: The EFS FilesSystem as the stateful shared storage of the Fargate service. Default: - create a new EFS FileSystem
        :param github: The github repository to clone as the doc root of the nginx. Default: https://github.com/cristurm/nyan-cat.git
        :param vpc: The VPC for the fargate service. Default: - create a new VPC
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d48c00a1c5a239742a3c89b521defba3212884e3f40c14dea1c32108fb92ada)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = StatefulFargateNginxProps(
            efs_file_system=efs_file_system, github=github, vpc=vpc
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="createSyncedAccessPoint")
    def create_synced_access_point(self) -> "SyncedAccessPoint":
        return typing.cast("SyncedAccessPoint", jsii.invoke(self, "createSyncedAccessPoint", []))


@jsii.data_type(
    jsii_type="cdk-efs-assets.StatefulFargateNginxProps",
    jsii_struct_bases=[],
    name_mapping={
        "efs_file_system": "efsFileSystem",
        "github": "github",
        "vpc": "vpc",
    },
)
class StatefulFargateNginxProps:
    def __init__(
        self,
        *,
        efs_file_system: typing.Optional[_aws_cdk_aws_efs_ceddda9d.IFileSystem] = None,
        github: typing.Optional[builtins.str] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    ) -> None:
        '''
        :param efs_file_system: The EFS FilesSystem as the stateful shared storage of the Fargate service. Default: - create a new EFS FileSystem
        :param github: The github repository to clone as the doc root of the nginx. Default: https://github.com/cristurm/nyan-cat.git
        :param vpc: The VPC for the fargate service. Default: - create a new VPC
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__165002c17438665d1eba2988c3a9dfcc5a9a73c1a69aeede3838d07a0c747966)
            check_type(argname="argument efs_file_system", value=efs_file_system, expected_type=type_hints["efs_file_system"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if efs_file_system is not None:
            self._values["efs_file_system"] = efs_file_system
        if github is not None:
            self._values["github"] = github
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def efs_file_system(self) -> typing.Optional[_aws_cdk_aws_efs_ceddda9d.IFileSystem]:
        '''The EFS FilesSystem as the stateful shared storage of the Fargate service.

        :default: - create a new EFS FileSystem
        '''
        result = self._values.get("efs_file_system")
        return typing.cast(typing.Optional[_aws_cdk_aws_efs_ceddda9d.IFileSystem], result)

    @builtins.property
    def github(self) -> typing.Optional[builtins.str]:
        '''The github repository to clone as the doc root of the nginx.

        :default: https://github.com/cristurm/nyan-cat.git
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''The VPC for the fargate service.

        :default: - create a new VPC
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StatefulFargateNginxProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk-efs-assets.SyncEngine")
class SyncEngine(enum.Enum):
    FARGATE = "FARGATE"
    LAMBDA = "LAMBDA"


class SyncSource(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="cdk-efs-assets.SyncSource",
):
    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="github")
    @builtins.classmethod
    def github(
        cls,
        *,
        repository: builtins.str,
        secret: typing.Optional[typing.Union[GithubSecret, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        sync_directory_path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> "SyncSource":
        '''
        :param repository: The github repository HTTP URI.
        :param secret: The github secret for the private repository.
        :param vpc: The VPC of the Amazon EFS Filesystem.
        :param sync_directory_path: The (absolute) directory path inside the EFS AccessPoint to sync files to. Specify '/' to restore synced files to the root directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default behavior is to restore to a directory matching the name of the repository)
        :param timeout: Timeout duration for sync Lambda function. (optional, default: Duration.minutes(3))
        :param vpc_subnets: Where to place the network interfaces within the VPC.
        '''
        props = GithubSourceProps(
            repository=repository,
            secret=secret,
            vpc=vpc,
            sync_directory_path=sync_directory_path,
            timeout=timeout,
            vpc_subnets=vpc_subnets,
        )

        return typing.cast("SyncSource", jsii.sinvoke(cls, "github", [props]))

    @jsii.member(jsii_name="s3Archive")
    @builtins.classmethod
    def s3_archive(
        cls,
        *,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        zip_file_path: builtins.str,
        sync_on_update: typing.Optional[builtins.bool] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        sync_directory_path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> "SyncSource":
        '''
        :param bucket: The S3 bucket containing the archive file.
        :param zip_file_path: The path of the zip file to extract in the S3 bucket.
        :param sync_on_update: If this is set to true, then whenever a new object is uploaded to the specified path, an EFS sync will be triggered. Currently, this functionality depends on at least one CloudTrail Trail existing in your account that captures the S3 event. The option is only available with the ``LAMBDA`` sync engine. Default: true
        :param vpc: The VPC of the Amazon EFS Filesystem.
        :param sync_directory_path: The (absolute) directory path inside the EFS AccessPoint to sync files to. Specify '/' to restore synced files to the root directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default behavior is to restore to a directory matching the name of the repository)
        :param timeout: Timeout duration for sync Lambda function. (optional, default: Duration.minutes(3))
        :param vpc_subnets: Where to place the network interfaces within the VPC.
        '''
        props = S3ArchiveSourceProps(
            bucket=bucket,
            zip_file_path=zip_file_path,
            sync_on_update=sync_on_update,
            vpc=vpc,
            sync_directory_path=sync_directory_path,
            timeout=timeout,
            vpc_subnets=vpc_subnets,
        )

        return typing.cast("SyncSource", jsii.sinvoke(cls, "s3Archive", [props]))


class _SyncSourceProxy(SyncSource):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, SyncSource).__jsii_proxy_class__ = lambda : _SyncSourceProxy


@jsii.data_type(
    jsii_type="cdk-efs-assets.SyncSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "vpc": "vpc",
        "sync_directory_path": "syncDirectoryPath",
        "timeout": "timeout",
        "vpc_subnets": "vpcSubnets",
    },
)
class SyncSourceProps:
    def __init__(
        self,
        *,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        sync_directory_path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param vpc: The VPC of the Amazon EFS Filesystem.
        :param sync_directory_path: The (absolute) directory path inside the EFS AccessPoint to sync files to. Specify '/' to restore synced files to the root directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default behavior is to restore to a directory matching the name of the repository)
        :param timeout: Timeout duration for sync Lambda function. (optional, default: Duration.minutes(3))
        :param vpc_subnets: Where to place the network interfaces within the VPC.
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f10bcebb6d3d0a369ec980b1c37bb55e376fd5877444423dc3d816991a446f4)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument sync_directory_path", value=sync_directory_path, expected_type=type_hints["sync_directory_path"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
        }
        if sync_directory_path is not None:
            self._values["sync_directory_path"] = sync_directory_path
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''The VPC of the Amazon EFS Filesystem.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def sync_directory_path(self) -> typing.Optional[builtins.str]:
        '''The (absolute) directory path inside the EFS AccessPoint to sync files to.

        Specify '/' to restore synced files to the root
        directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default
        behavior is to restore to a directory matching the name of the repository)
        '''
        result = self._values.get("sync_directory_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''Timeout duration for sync Lambda function.

        (optional, default: Duration.minutes(3))
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''Where to place the network interfaces within the VPC.'''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyncSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_aws_efs_ceddda9d.IAccessPoint)
class SyncedAccessPoint(
    _aws_cdk_aws_efs_ceddda9d.AccessPoint,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-efs-assets.SyncedAccessPoint",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        sync_source: SyncSource,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        engine: typing.Optional[SyncEngine] = None,
        file_system: _aws_cdk_aws_efs_ceddda9d.IFileSystem,
        create_acl: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.Acl, typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param sync_source: 
        :param vpc: The VPC to run the sync job.
        :param engine: Trigger the sync with AWS Lambda or AWS Fargate.
        :param file_system: The efs filesystem.
        :param create_acl: Specifies the POSIX IDs and permissions to apply when creating the access point's root directory. If the root directory specified by ``path`` does not exist, EFS creates the root directory and applies the permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``. Default: - None. The directory specified by ``path`` must exist.
        :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. Default: '/'
        :param posix_user: The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point. Specify this to enforce a user identity using an access point. Default: - user identity not enforced
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e2a706dda6a786990e0d3a572c4426dc6d6f4234c62760d8e85b3607819652c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SyncedAccessPointProps(
            sync_source=sync_source,
            vpc=vpc,
            engine=engine,
            file_system=file_system,
            create_acl=create_acl,
            path=path,
            posix_user=posix_user,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk-efs-assets.SyncedAccessPointProps",
    jsii_struct_bases=[_aws_cdk_aws_efs_ceddda9d.AccessPointProps],
    name_mapping={
        "create_acl": "createAcl",
        "path": "path",
        "posix_user": "posixUser",
        "file_system": "fileSystem",
        "sync_source": "syncSource",
        "vpc": "vpc",
        "engine": "engine",
    },
)
class SyncedAccessPointProps(_aws_cdk_aws_efs_ceddda9d.AccessPointProps):
    def __init__(
        self,
        *,
        create_acl: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.Acl, typing.Dict[builtins.str, typing.Any]]] = None,
        path: typing.Optional[builtins.str] = None,
        posix_user: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
        file_system: _aws_cdk_aws_efs_ceddda9d.IFileSystem,
        sync_source: SyncSource,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        engine: typing.Optional[SyncEngine] = None,
    ) -> None:
        '''
        :param create_acl: Specifies the POSIX IDs and permissions to apply when creating the access point's root directory. If the root directory specified by ``path`` does not exist, EFS creates the root directory and applies the permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``. Default: - None. The directory specified by ``path`` must exist.
        :param path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. Default: '/'
        :param posix_user: The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point. Specify this to enforce a user identity using an access point. Default: - user identity not enforced
        :param file_system: The efs filesystem.
        :param sync_source: 
        :param vpc: The VPC to run the sync job.
        :param engine: Trigger the sync with AWS Lambda or AWS Fargate.
        '''
        if isinstance(create_acl, dict):
            create_acl = _aws_cdk_aws_efs_ceddda9d.Acl(**create_acl)
        if isinstance(posix_user, dict):
            posix_user = _aws_cdk_aws_efs_ceddda9d.PosixUser(**posix_user)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bfc602fdadc88a0326aa20dd4908d83ddaf0d71081c09464d628e3afa1216bb)
            check_type(argname="argument create_acl", value=create_acl, expected_type=type_hints["create_acl"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument posix_user", value=posix_user, expected_type=type_hints["posix_user"])
            check_type(argname="argument file_system", value=file_system, expected_type=type_hints["file_system"])
            check_type(argname="argument sync_source", value=sync_source, expected_type=type_hints["sync_source"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system": file_system,
            "sync_source": sync_source,
            "vpc": vpc,
        }
        if create_acl is not None:
            self._values["create_acl"] = create_acl
        if path is not None:
            self._values["path"] = path
        if posix_user is not None:
            self._values["posix_user"] = posix_user
        if engine is not None:
            self._values["engine"] = engine

    @builtins.property
    def create_acl(self) -> typing.Optional[_aws_cdk_aws_efs_ceddda9d.Acl]:
        '''Specifies the POSIX IDs and permissions to apply when creating the access point's root directory.

        If the
        root directory specified by ``path`` does not exist, EFS creates the root directory and applies the
        permissions specified here. If the specified ``path`` does not exist, you must specify ``createAcl``.

        :default: - None. The directory specified by ``path`` must exist.
        '''
        result = self._values.get("create_acl")
        return typing.cast(typing.Optional[_aws_cdk_aws_efs_ceddda9d.Acl], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system.

        :default: '/'
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_user(self) -> typing.Optional[_aws_cdk_aws_efs_ceddda9d.PosixUser]:
        '''The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.

        Specify this to enforce a user identity using an access point.

        :default: - user identity not enforced

        :see: - `Enforcing a User Identity Using an Access Point <https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html>`_
        '''
        result = self._values.get("posix_user")
        return typing.cast(typing.Optional[_aws_cdk_aws_efs_ceddda9d.PosixUser], result)

    @builtins.property
    def file_system(self) -> _aws_cdk_aws_efs_ceddda9d.IFileSystem:
        '''The efs filesystem.'''
        result = self._values.get("file_system")
        assert result is not None, "Required property 'file_system' is missing"
        return typing.cast(_aws_cdk_aws_efs_ceddda9d.IFileSystem, result)

    @builtins.property
    def sync_source(self) -> SyncSource:
        result = self._values.get("sync_source")
        assert result is not None, "Required property 'sync_source' is missing"
        return typing.cast(SyncSource, result)

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''The VPC to run the sync job.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def engine(self) -> typing.Optional[SyncEngine]:
        '''Trigger the sync with AWS Lambda or AWS Fargate.'''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[SyncEngine], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyncedAccessPointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-efs-assets.GithubSourceProps",
    jsii_struct_bases=[SyncSourceProps],
    name_mapping={
        "vpc": "vpc",
        "sync_directory_path": "syncDirectoryPath",
        "timeout": "timeout",
        "vpc_subnets": "vpcSubnets",
        "repository": "repository",
        "secret": "secret",
    },
)
class GithubSourceProps(SyncSourceProps):
    def __init__(
        self,
        *,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        sync_directory_path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        repository: builtins.str,
        secret: typing.Optional[typing.Union[GithubSecret, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param vpc: The VPC of the Amazon EFS Filesystem.
        :param sync_directory_path: The (absolute) directory path inside the EFS AccessPoint to sync files to. Specify '/' to restore synced files to the root directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default behavior is to restore to a directory matching the name of the repository)
        :param timeout: Timeout duration for sync Lambda function. (optional, default: Duration.minutes(3))
        :param vpc_subnets: Where to place the network interfaces within the VPC.
        :param repository: The github repository HTTP URI.
        :param secret: The github secret for the private repository.
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
        if isinstance(secret, dict):
            secret = GithubSecret(**secret)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d06d70b7ebaca3773b9bfa767d43246e698e949ef483da58182f94bcafb6c14)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument sync_directory_path", value=sync_directory_path, expected_type=type_hints["sync_directory_path"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
            "repository": repository,
        }
        if sync_directory_path is not None:
            self._values["sync_directory_path"] = sync_directory_path
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''The VPC of the Amazon EFS Filesystem.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def sync_directory_path(self) -> typing.Optional[builtins.str]:
        '''The (absolute) directory path inside the EFS AccessPoint to sync files to.

        Specify '/' to restore synced files to the root
        directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default
        behavior is to restore to a directory matching the name of the repository)
        '''
        result = self._values.get("sync_directory_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''Timeout duration for sync Lambda function.

        (optional, default: Duration.minutes(3))
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''Where to place the network interfaces within the VPC.'''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''The github repository HTTP URI.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret(self) -> typing.Optional[GithubSecret]:
        '''The github secret for the private repository.'''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[GithubSecret], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GithubSyncSource(
    SyncSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-efs-assets.GithubSyncSource",
):
    def __init__(
        self,
        *,
        repository: builtins.str,
        secret: typing.Optional[typing.Union[GithubSecret, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        sync_directory_path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param repository: The github repository HTTP URI.
        :param secret: The github secret for the private repository.
        :param vpc: The VPC of the Amazon EFS Filesystem.
        :param sync_directory_path: The (absolute) directory path inside the EFS AccessPoint to sync files to. Specify '/' to restore synced files to the root directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default behavior is to restore to a directory matching the name of the repository)
        :param timeout: Timeout duration for sync Lambda function. (optional, default: Duration.minutes(3))
        :param vpc_subnets: Where to place the network interfaces within the VPC.
        '''
        props = GithubSourceProps(
            repository=repository,
            secret=secret,
            vpc=vpc,
            sync_directory_path=sync_directory_path,
            timeout=timeout,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [props])


@jsii.data_type(
    jsii_type="cdk-efs-assets.S3ArchiveSourceProps",
    jsii_struct_bases=[SyncSourceProps],
    name_mapping={
        "vpc": "vpc",
        "sync_directory_path": "syncDirectoryPath",
        "timeout": "timeout",
        "vpc_subnets": "vpcSubnets",
        "bucket": "bucket",
        "zip_file_path": "zipFilePath",
        "sync_on_update": "syncOnUpdate",
    },
)
class S3ArchiveSourceProps(SyncSourceProps):
    def __init__(
        self,
        *,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        sync_directory_path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        zip_file_path: builtins.str,
        sync_on_update: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param vpc: The VPC of the Amazon EFS Filesystem.
        :param sync_directory_path: The (absolute) directory path inside the EFS AccessPoint to sync files to. Specify '/' to restore synced files to the root directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default behavior is to restore to a directory matching the name of the repository)
        :param timeout: Timeout duration for sync Lambda function. (optional, default: Duration.minutes(3))
        :param vpc_subnets: Where to place the network interfaces within the VPC.
        :param bucket: The S3 bucket containing the archive file.
        :param zip_file_path: The path of the zip file to extract in the S3 bucket.
        :param sync_on_update: If this is set to true, then whenever a new object is uploaded to the specified path, an EFS sync will be triggered. Currently, this functionality depends on at least one CloudTrail Trail existing in your account that captures the S3 event. The option is only available with the ``LAMBDA`` sync engine. Default: true
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86b8fbbc6b8481516fb62baae61fbbddce5af2d2fb921d8fa2a72d9a2f989c4)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument sync_directory_path", value=sync_directory_path, expected_type=type_hints["sync_directory_path"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument zip_file_path", value=zip_file_path, expected_type=type_hints["zip_file_path"])
            check_type(argname="argument sync_on_update", value=sync_on_update, expected_type=type_hints["sync_on_update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
            "bucket": bucket,
            "zip_file_path": zip_file_path,
        }
        if sync_directory_path is not None:
            self._values["sync_directory_path"] = sync_directory_path
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets
        if sync_on_update is not None:
            self._values["sync_on_update"] = sync_on_update

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''The VPC of the Amazon EFS Filesystem.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def sync_directory_path(self) -> typing.Optional[builtins.str]:
        '''The (absolute) directory path inside the EFS AccessPoint to sync files to.

        Specify '/' to restore synced files to the root
        directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default
        behavior is to restore to a directory matching the name of the repository)
        '''
        result = self._values.get("sync_directory_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''Timeout duration for sync Lambda function.

        (optional, default: Duration.minutes(3))
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''Where to place the network interfaces within the VPC.'''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    @builtins.property
    def bucket(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        '''The S3 bucket containing the archive file.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, result)

    @builtins.property
    def zip_file_path(self) -> builtins.str:
        '''The path of the zip file to extract in the S3 bucket.'''
        result = self._values.get("zip_file_path")
        assert result is not None, "Required property 'zip_file_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sync_on_update(self) -> typing.Optional[builtins.bool]:
        '''If this is set to true, then whenever a new object is uploaded to the specified path, an EFS sync will be triggered.

        Currently, this functionality depends on at least one CloudTrail Trail
        existing in your account that captures the S3 event.

        The option is only available with the ``LAMBDA`` sync engine.

        :default: true
        '''
        result = self._values.get("sync_on_update")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ArchiveSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ArchiveSyncSource(
    SyncSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-efs-assets.S3ArchiveSyncSource",
):
    def __init__(
        self,
        *,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        zip_file_path: builtins.str,
        sync_on_update: typing.Optional[builtins.bool] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        sync_directory_path: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket: The S3 bucket containing the archive file.
        :param zip_file_path: The path of the zip file to extract in the S3 bucket.
        :param sync_on_update: If this is set to true, then whenever a new object is uploaded to the specified path, an EFS sync will be triggered. Currently, this functionality depends on at least one CloudTrail Trail existing in your account that captures the S3 event. The option is only available with the ``LAMBDA`` sync engine. Default: true
        :param vpc: The VPC of the Amazon EFS Filesystem.
        :param sync_directory_path: The (absolute) directory path inside the EFS AccessPoint to sync files to. Specify '/' to restore synced files to the root directory. (optional, default: a source-specific directory path. For example, for the GitHub source, the default behavior is to restore to a directory matching the name of the repository)
        :param timeout: Timeout duration for sync Lambda function. (optional, default: Duration.minutes(3))
        :param vpc_subnets: Where to place the network interfaces within the VPC.
        '''
        props = S3ArchiveSourceProps(
            bucket=bucket,
            zip_file_path=zip_file_path,
            sync_on_update=sync_on_update,
            vpc=vpc,
            sync_directory_path=sync_directory_path,
            timeout=timeout,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [props])


__all__ = [
    "EfsFargateSite",
    "EfsFargateSiteProps",
    "EfsFargateTask",
    "EfsFargateTaskProps",
    "FargateTaskConfig",
    "GithubSecret",
    "GithubSourceProps",
    "GithubSyncSource",
    "S3ArchiveSourceProps",
    "S3ArchiveSyncSource",
    "StatefulFargateNginx",
    "StatefulFargateNginxProps",
    "SyncEngine",
    "SyncSource",
    "SyncSourceProps",
    "SyncedAccessPoint",
    "SyncedAccessPointProps",
]

publication.publish()

def _typecheckingstub__d6a20ce890668e81b5e889b725552e04817338b13b4a8d701527047b099d24c5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
    task: _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad14ca58a5088c5b480664cae28f48c52f45edbaa2494286fcfa0958682904e(
    *,
    access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
    task: _aws_cdk_aws_ecs_ceddda9d.FargateTaskDefinition,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea248b6c4413e2452dfed8d02ea535672572b6e000823ed4a98be4b443a24f0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
    sync_container: typing.Union[_aws_cdk_aws_ecs_ceddda9d.ContainerDefinitionOptions, typing.Dict[builtins.str, typing.Any]],
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    efs_mount_target: typing.Optional[builtins.str] = None,
    secret: typing.Optional[typing.Union[GithubSecret, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f197af0923d3303af0c30ff7435b02b6cf7fd5be713fc1b89d0d9e4793e0cb50(
    *,
    access_point: _aws_cdk_aws_efs_ceddda9d.AccessPoint,
    sync_container: typing.Union[_aws_cdk_aws_ecs_ceddda9d.ContainerDefinitionOptions, typing.Dict[builtins.str, typing.Any]],
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    efs_mount_target: typing.Optional[builtins.str] = None,
    secret: typing.Optional[typing.Union[GithubSecret, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a49c6dadc8eec97c51e0ff9e68eb9f8bfad4923a6dfc282ac262c2d162e8b0(
    *,
    security_group: _aws_cdk_aws_ec2_ceddda9d.ISecurityGroup,
    task: _aws_cdk_aws_ecs_ceddda9d.TaskDefinition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac7dfb8948f0cafd529ea5ab43067c550dd6bc8a8b653dcbd78d388e2ce930b(
    *,
    id: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d48c00a1c5a239742a3c89b521defba3212884e3f40c14dea1c32108fb92ada(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    efs_file_system: typing.Optional[_aws_cdk_aws_efs_ceddda9d.IFileSystem] = None,
    github: typing.Optional[builtins.str] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165002c17438665d1eba2988c3a9dfcc5a9a73c1a69aeede3838d07a0c747966(
    *,
    efs_file_system: typing.Optional[_aws_cdk_aws_efs_ceddda9d.IFileSystem] = None,
    github: typing.Optional[builtins.str] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f10bcebb6d3d0a369ec980b1c37bb55e376fd5877444423dc3d816991a446f4(
    *,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    sync_directory_path: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2a706dda6a786990e0d3a572c4426dc6d6f4234c62760d8e85b3607819652c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    sync_source: SyncSource,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    engine: typing.Optional[SyncEngine] = None,
    file_system: _aws_cdk_aws_efs_ceddda9d.IFileSystem,
    create_acl: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.Acl, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bfc602fdadc88a0326aa20dd4908d83ddaf0d71081c09464d628e3afa1216bb(
    *,
    create_acl: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.Acl, typing.Dict[builtins.str, typing.Any]]] = None,
    path: typing.Optional[builtins.str] = None,
    posix_user: typing.Optional[typing.Union[_aws_cdk_aws_efs_ceddda9d.PosixUser, typing.Dict[builtins.str, typing.Any]]] = None,
    file_system: _aws_cdk_aws_efs_ceddda9d.IFileSystem,
    sync_source: SyncSource,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    engine: typing.Optional[SyncEngine] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d06d70b7ebaca3773b9bfa767d43246e698e949ef483da58182f94bcafb6c14(
    *,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    sync_directory_path: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    repository: builtins.str,
    secret: typing.Optional[typing.Union[GithubSecret, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86b8fbbc6b8481516fb62baae61fbbddce5af2d2fb921d8fa2a72d9a2f989c4(
    *,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    sync_directory_path: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    zip_file_path: builtins.str,
    sync_on_update: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
