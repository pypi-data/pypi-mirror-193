local ciImageRegistry = '%HB_IMAGE_REGISTRY%';
local ciDnsServers = ['%HB_CI_DNS%'];
local hostbutterCiImage = ciImageRegistry + '/fresh2dev/hostbutter-ci:%HB_VERSION%';

// PARAMETERS
local domains = std.parseJson(std.extVar('input.domains'));
local domainTriggers = std.parseJson(std.extVar('input.domainTriggers'));
local domainClusterMap = std.parseJson(std.extVar('input.domainClusterMap'));
local dockerHubUser = std.extVar('input.dockerHubUser');
local secrets = std.parseJson(std.extVar('input.secrets'));
local secretFiles = std.parseJson(std.extVar('input.secretFiles'));
local volumes = std.parseJson(std.extVar('input.volumes'));
local beforeSteps = std.parseJson(std.extVar('input.beforeSteps'));
local afterSteps = std.parseJson(std.extVar('input.afterSteps'));
local finalSteps = std.parseJson(std.extVar('input.finalSteps'));
local extraObjects = std.parseJson(std.extVar('input.extraObjects'));

local domainList = if domains != null && std.length(domains) > 0 then domains else [k for k in std.objectFieldsAll(domainTriggers)];
local sharedDockerConfigDir = '/.docker';

// // START DEBUG VARS
// local domainTriggers={"lokalhost.net": {}};
// local domainClusterMap={"example.com": "lokalhost.net"};
// dockerHubUser="donald;"
// local secrets=["testing"];
// local secretFiles={"THIS_VAR":"that.yml"};
// local volumes=[];
// local beforeSteps=[{
//   "name": "publish-testpypi",
//   "image": "registry.lokalhost.net/python:3.9.13",
//   "commands": [
//     "echo -n \"$PYPI_CREDS\" > ~/.pypirc",
//     "make publish"
//   ],
//   "when": {
//     "branch": ["main", "master"],
//     "event": ["push", "custom"]
//   }
// }];
// local afterSteps=[];
// local finalSteps=[];
// local extraObjects=[];
// local extraSecrets=[
//       {
//         "kind": "secret",
//         "name": "NETLIFY_CREDS",
//         "get": {
//           "path": "secret/data/3p",
//           "name": "NETLIFY_CREDS"
//         }
//       }
//     ];
// local gitSshKey='default';
// local ciImageRegistry='registry.lokalhost.net';

// END DEBUG VARS

local targetConditions = {
  [e]: (if !std.objectHas(domainTriggers, e) then {} else domainTriggers[e])
  for e in domainList
};

local new_secret(name, alias, path) = {
  kind: 'secret',
  name: (if std.length(alias) > 0 then alias else name),
  get: {
    path: path,
    name: name,
  },
};

local get_or_default(obj, k, d) = if std.objectHas(obj, k) then obj[k] else d;


local allSecretNames = secrets + [secretFiles[k] for k in std.objectFieldsAll(secretFiles)];

local allSecrets = [
  new_secret(alias='CI_PRIVATE_KEY', name='CI_PRIVATE_KEY', path='secret/data/hostbutter/global'),
  new_secret(alias='DOCKER_CONFIG_JSON', name='DOCKER_CONFIG_JSON', path='secret/data/hostbutter/global'),
] + [
  secret
  for cluster in std.uniq([get_or_default(domainClusterMap, d, d) for d in domainList])
  for secret in [
    new_secret(alias=cluster + '_' + 'SWARM_MANAGER', name='SWARM_MANAGER', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'SWARM_MANAGER_SSH_PORT', name='SWARM_MANAGER_SSH_PORT', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'SWARM_USER', name='SWARM_USER', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'HB_PROXY_NETWORK', name='HB_PROXY_NETWORK', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'HB_NFS_OPTS', name='HB_NFS_OPTS', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'HB_NAS_ROOT_MOUNTPOINT', name='HB_NAS_ROOT_MOUNTPOINT', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'HB_IMAGE_REGISTRY', name='HB_IMAGE_REGISTRY', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'HB_IMAGE_OWNER', name='HB_IMAGE_OWNER', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'PUID', name='PUID', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'PGID', name='PGID', path='secret/data/hostbutter/clusters/' + cluster),
    new_secret(alias=cluster + '_' + 'TZ', name='TZ', path='secret/data/hostbutter/clusters/' + cluster),
  ]
] + [
  new_secret(alias=d + '_' + s, name=s, path='secret/data/hostbutter/projects/' + d + '/${DRONE_REPO}')
  for d in domainList
  for s in std.uniq(std.sort(allSecretNames))
];

local new_build_env(cluster) = {
  TARGET_DOCKER_CLUSTER: cluster,
  DOCKER_CONFIG: sharedDockerConfigDir,
  CI_PRIVATE_KEY: {
    from_secret: 'CI_PRIVATE_KEY',
  },
  HB_PROXY_NETWORK: {
    from_secret: cluster + '_' + 'HB_PROXY_NETWORK',
  },
  HB_NFS_OPTS: {
    from_secret: cluster + '_' + 'HB_NFS_OPTS',
  },
  HB_NAS_ROOT_MOUNTPOINT: {
    from_secret: cluster + '_' + 'HB_NAS_ROOT_MOUNTPOINT',
  },
  HB_IMAGE_REGISTRY: {
    from_secret: cluster + '_' + 'HB_IMAGE_REGISTRY',
  },
  HB_IMAGE_OWNER: {
    from_secret: cluster + '_' + 'HB_IMAGE_OWNER',
  },
  SWARM_MANAGER: {
    from_secret: cluster + '_' + 'SWARM_MANAGER',
  },
  SWARM_MANAGER_SSH_PORT: {
    from_secret: cluster + '_' + 'SWARM_MANAGER_SSH_PORT',
  },
  SWARM_USER: {
    from_secret: cluster + '_' + 'SWARM_USER',
  },
  PUID: {
    from_secret: cluster + '_' + 'PUID',
  },
  PGID: {
    from_secret: cluster + '_' + 'PGID',
  },
  TZ: {
    from_secret: cluster + '_' + 'TZ',
  },
};

local buildEnvs = {
  [d]: { HB_DOMAIN: d } + new_build_env(cluster=get_or_default(domainClusterMap, d, d))
  for d in domainList
};

local dockerConfig = [
  {
    name: 'docker-config',
    path: sharedDockerConfigDir,
  },
  {
    name: 'docker-socket',
    path: '/var/run',
  },
];

local dockerCache = [
  {
    name: 'docker-cache',
    path: '/cache',
  },
];


local gitSshKeyCmds = [
  '[ ! -z "$CI_PRIVATE_KEY" ] || (echo "error; CI_PRIVATE_KEY is empty; aborting." && exit 1)',
  'mkdir -p ~/.ssh',
  'echo -n "$CI_PRIVATE_KEY" > ~/.ssh/id_ed25519',
  'echo "Host *" > ~/.ssh/config',
  'echo "    StrictHostKeyChecking no" >> ~/.ssh/config',
  'chmod -R 400 ~/.ssh',
  '[ -d .git ] || (git clone -b ${DRONE_BRANCH:-$DRONE_REPO_BRANCH} ${DRONE_GIT_SSH_URL} . && git checkout ${DRONE_COMMIT} && git submodule update --init --recursive)',
  'mv ~/.ssh ./',
  'git config core.sshCommand "ssh -F ./.ssh/config -i ./.ssh/id_ed25519"',
];

local prepSteps = [
  {
    name: 'clone',
    image: ciImageRegistry + '/alpine/git:2.36.3',
    environment: {
      CI_PRIVATE_KEY: {
        from_secret: 'CI_PRIVATE_KEY',
      },
    },
    commands: gitSshKeyCmds,
  },
  {
    name: 'DinD',
    image: ciImageRegistry + '/docker:20.10.23-dind',
    privileged: true,
    detach: true,
    volumes: dockerConfig,
    environment: {
      DOCKER_CONFIG: sharedDockerConfigDir,
      DOCKER_CONFIG_JSON: {
        from_secret: 'DOCKER_CONFIG_JSON',
      },
    },
    commands: [
      '[ ! -z "$DOCKER_CONFIG_JSON" ] || (echo "Docker config var is empty." && exit 1)',
      'echo "$DOCKER_CONFIG_JSON" > "$DOCKER_CONFIG/config.json"',
      // 'docker context create DinD --docker host="tcp://DinD:2375"',
      'docker context create DinD --docker host="unix:///var/run/DinD.sock"',
      'docker context use DinD',
      // 'dockerd --tls=false --dns 192.168.69.25 -H tcp://DinD:2375',
      'dockerd --dns ' + std.join(' --dns ', ciDnsServers) + ' -H unix:///var/run/DinD.sock',
    ],
  },
  {
    name: 'DinD-wait',
    image: hostbutterCiImage,
    volumes: dockerConfig,
    environment: {
      DOCKER_CONFIG: sharedDockerConfigDir,
    },
    commands: [
      'export DOCKER_CONTEXT="DinD"',
      'while ! docker info &> /dev/null; do echo "waiting for docker" && sleep 3s; done',
      'docker info',
    ],
  },
];

local build_env_steps(domain, domainTrigger={}) = [
  {
    name: domain + '_' + 'git-reset',
    image: ciImageRegistry + '/alpine/git:2.36.3',
    environment: {
      CI_PRIVATE_KEY: {
        from_secret: 'CI_PRIVATE_KEY',
      },
    },
    commands: [
      'git reset --hard',
      'git clean -fd',
    ] + gitSshKeyCmds,
    when: domainTrigger,  // <-- always reset
  },
  {
    name: domain + '_' + 'pull-project-secrets',
    image: ciImageRegistry + '/alpine/git:2.36.3',
    environment: {
      [k]: { from_secret: domain + '_' + secretFiles[k] }
      for k in std.objectFieldsAll(secretFiles)
    },
    commands: [
      '([ ! -z "$' + k + '" ] && mkdir -p secrets-' + domain + '/ && echo -n "$' + k + '" > "secrets-' + domain + '/' + secretFiles[k] + '") || (echo "error: "' + k + '" key from vault is missing or empty for this project." && exit 1)'
      for k in std.objectFieldsAll(secretFiles)
    ],
    when: domainTrigger,
  },
] + [
  s { name: domain + '_' + s.name, when: domainTrigger, environment: buildEnvs[domain] + (if std.objectHas(s, 'environment') then s.environment else {}) }
  for s in beforeSteps
] + [
  {
    name: domain + '_' + 'build-image',
    image: hostbutterCiImage,
    environment: buildEnvs[domain],
    volumes: dockerConfig,
    commands: [
      '[ ! -f "Dockerfile" ] || (butter -c DinD stack-build --tag-version "${DRONE_TAG}" --registry "$HB_IMAGE_REGISTRY")',
    ],
    when: domainTrigger,
  },
  {
    name: domain + '_' + 'deploy-stack',
    image: hostbutterCiImage,
    environment: buildEnvs[domain],
    volumes: dockerConfig,
    commands: [
      'set -o pipefail',
      '[ ! -z "$CI_PRIVATE_KEY" ] || (echo "Swarm user-key var is empty." && exit 1)',
      '[ ! -z "$SWARM_MANAGER" ] || (echo "Swarm manager var is empty." && exit 1)',
      '[ ! -z "$SWARM_USER" ] || (echo "Swarm user var is empty." && exit 1)',
      '[ -f .env ] || (echo "File not found: .env" && exit 1)',
      'mkdir -p ~/.ssh',
      'ssh-keyscan -p $SWARM_MANAGER_SSH_PORT $SWARM_MANAGER > ~/.ssh/known_hosts',
      'echo -n "$CI_PRIVATE_KEY" > ~/.ssh/id_ed25519',
      'chmod 400 -R ~/.ssh',
      'docker context create $TARGET_DOCKER_CLUSTER --docker host="ssh://$SWARM_USER@$SWARM_MANAGER:$SWARM_MANAGER_SSH_PORT"',
      '! ls docker-compose*.y*ml 1>/dev/null 2>&1 || butter -c $TARGET_DOCKER_CLUSTER stack-up',
    ],
    when: domainTrigger,
  },
] + [
  s { name: domain + '_' + s.name, when: domainTrigger, environment: buildEnvs[domain] + (if std.objectHas(s, 'environment') then s.environment else {}) }
  for s in afterSteps
];

local steps = [
  envSteps
  for d in domainList
  for envSteps in build_env_steps(domain=d, domainTrigger=targetConditions[d])
];

local publishDockerHubSteps = if dockerHubUser == null || std.length(dockerHubUser) == 0 || std.length(domainList) == 0 then [] else [
  {
    name: 'publish-dockerhub',
    image: hostbutterCiImage,
    // use build environment from first domain;
    // this determines the source image registry.
    environment: buildEnvs[domains[0]],
    volumes: dockerConfig,
    commands: [
      'butter -c DinD registry-import "$HB_IMAGE_REGISTRY/${DRONE_REPO}:${DRONE_TAG}" --skopeo-registry "' + ciImageRegistry + '" --registry "docker.io" --owner "' + dockerHubUser + '"',
    ],
    when: { event: 'tag' },
  },
];

local pipeline = {
  kind: 'pipeline',
  type: 'docker',
  platform: {
    os: 'linux',
    arch: 'amd64',
  },
  name: 'HostButter.net',
  image_pull_secrets: ['DOCKER_CONFIG_JSON'],
  clone: { disable: true },
  steps: prepSteps + steps + publishDockerHubSteps + finalSteps,
  volumes: [
    {
      name: 'docker-socket',
      temp: {},
    },
    {
      name: 'docker-config',
      temp: {},
    },
    {
      name: 'docker-cache',
      temp: {},
    },
  ] + volumes,
};

[pipeline] + allSecrets + extraObjects
