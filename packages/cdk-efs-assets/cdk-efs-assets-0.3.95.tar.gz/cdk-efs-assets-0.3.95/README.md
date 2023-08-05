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
