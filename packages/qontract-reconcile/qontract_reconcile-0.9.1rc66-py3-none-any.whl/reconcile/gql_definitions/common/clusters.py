"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)

from reconcile.gql_definitions.fragments.aws_infra_management_account import (
    AWSInfrastructureManagementAccount,
)
from reconcile.gql_definitions.fragments.jumphost_common_fields import (
    CommonJumphostFields,
)
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
fragment AWSInfrastructureManagementAccount on AWSInfrastructureManagementAccount_v1 {
  account {
    name
    uid
    terraformUsername
    resourcesDefaultRegion
    automationToken {
      ... VaultSecret
    }
  }
  accessLevel
  default
}

fragment CommonJumphostFields on ClusterJumpHost_v1 {
  hostname
  knownHosts
  user
  port
  remotePort
  identity {
    ... VaultSecret
  }
}

fragment VaultSecret on VaultSecret_v1 {
    path
    field
    version
    format
}

query Clusters($name: String) {
  clusters: clusters_v1(name: $name) {
    path
    name
    serverUrl
    consoleUrl
    kibanaUrl
    elbFQDN
    prometheusUrl
    managedGroups
    managedClusterRoles
    insecureSkipTLSVerify
    jumpHost {
      ... CommonJumphostFields
    }
    auth {
      service
      ... on ClusterAuthGithubOrg_v1 {
        org
      }
      ... on ClusterAuthGithubOrgTeam_v1 {
        org
        team
      }
      # ... on ClusterAuthOIDC_v1 {
      # }
    }
    ocm {
      name
      url
      accessTokenClientId
      accessTokenUrl
      accessTokenClientSecret {
        ... VaultSecret
      }
      blockedVersions
      inheritVersionData {
        name
        publishVersionData {
          name
        }
      }
      sectors {
        name
        dependencies {
          name
          ocm {
            name
          }
        }
      }
    }
    awsInfrastructureAccess {
      awsGroup {
        account {
          name
          uid
          terraformUsername
          automationToken {
            ... VaultSecret
          }
        }
        roles {
          users {
            org_username
          }
        }
      }
      accessLevel
    }
    awsInfrastructureManagementAccounts {
      ... AWSInfrastructureManagementAccount
    }
    spec {
      product
      hypershift
      ... on ClusterSpecOSD_v1 {
        storage
        load_balancers
      }
      ... on ClusterSpecROSA_v1 {
        subnet_ids
        availability_zones
        account {
          uid
          rosa {
            ocm_environments {
              ocm {
                name
              }
              creator_role_arn
              installer_role_arn
              support_role_arn
              controlplane_role_arn
              worker_role_arn
            }
          }
        }
      }
      id
      external_id
      provider
      region
      channel
      version
      initial_version
      multi_az
      nodes
      instance_type
      private
      provision_shard_id
      autoscale {
        min_replicas
        max_replicas
      }
      disable_user_workload_monitoring
    }
    externalConfiguration {
      labels
    }
    upgradePolicy {
      workloads
      schedule
      conditions {
        soakDays
        mutexes
        sector
      }
    }
    additionalRouters {
      private
      route_selectors
    }
    network {
      type
      vpc
      service
      pod
    }
    machinePools {
      id
      instance_type
      replicas
      labels
      taints {
        key
        value
        effect
      }
    }
    peering {
      connections {
        name
        provider
        manageRoutes
        delete
        ... on ClusterPeeringConnectionAccount_v1 {
          vpc {
            account {
              name
              uid
              terraformUsername
              automationToken {
                ... VaultSecret
              }
            }
            vpc_id
            cidr_block
            region
          }
          assumeRole
        }
        ... on ClusterPeeringConnectionAccountVPCMesh_v1 {
          account {
            name
            uid
            terraformUsername
            automationToken {
              ... VaultSecret
            }
          }
          tags
        }
        ... on ClusterPeeringConnectionAccountTGW_v1 {
          account {
            name
            uid
            terraformUsername
            automationToken {
              ... VaultSecret
            }
          }
          tags
          cidrBlock
          manageSecurityGroups
          assumeRole
        }
        ... on ClusterPeeringConnectionClusterRequester_v1 {
          cluster {
            name
            network {
              vpc
            }
            spec {
              region
            }
            awsInfrastructureAccess {
              awsGroup {
                account {
                  name
                  uid
                  terraformUsername
                  automationToken {
                    ... VaultSecret
                  }
                }
              }
              accessLevel
            }
            awsInfrastructureManagementAccounts {
              ... AWSInfrastructureManagementAccount
            }
            peering {
              connections {
                name
                provider
                manageRoutes
                ... on ClusterPeeringConnectionClusterAccepter_v1 {
                  name
                  cluster {
                    name
                  }
                  awsInfrastructureManagementAccount {
                    name
                    uid
                    terraformUsername
                    automationToken {
                      ... VaultSecret
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    addons {
      name
      parameters {
        id
        value
      }
    }
    automationToken {
      ... VaultSecret
    }
    clusterAdmin
    clusterAdminAutomationToken {
      ... VaultSecret
    }
    internal
    disable {
      e2eTests
      integrations
    }
  }
}
"""


class ClusterAuthV1(BaseModel):
    service: str = Field(..., alias="service")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAuthGithubOrgV1(ClusterAuthV1):
    org: str = Field(..., alias="org")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAuthGithubOrgTeamV1(ClusterAuthV1):
    org: str = Field(..., alias="org")
    team: str = Field(..., alias="team")

    class Config:
        smart_union = True
        extra = Extra.forbid


class OpenShiftClusterManagerV1_OpenShiftClusterManagerV1_OpenShiftClusterManagerV1(
    BaseModel
):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class OpenShiftClusterManagerV1_OpenShiftClusterManagerV1(BaseModel):
    name: str = Field(..., alias="name")
    publish_version_data: Optional[
        list[
            OpenShiftClusterManagerV1_OpenShiftClusterManagerV1_OpenShiftClusterManagerV1
        ]
    ] = Field(..., alias="publishVersionData")

    class Config:
        smart_union = True
        extra = Extra.forbid


class OpenShiftClusterManagerSectorDependenciesV1_OpenShiftClusterManagerV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class OpenShiftClusterManagerSectorDependenciesV1(BaseModel):
    name: str = Field(..., alias="name")
    ocm: Optional[
        OpenShiftClusterManagerSectorDependenciesV1_OpenShiftClusterManagerV1
    ] = Field(..., alias="ocm")

    class Config:
        smart_union = True
        extra = Extra.forbid


class OpenShiftClusterManagerSectorV1(BaseModel):
    name: str = Field(..., alias="name")
    dependencies: Optional[list[OpenShiftClusterManagerSectorDependenciesV1]] = Field(
        ..., alias="dependencies"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class OpenShiftClusterManagerV1(BaseModel):
    name: str = Field(..., alias="name")
    url: str = Field(..., alias="url")
    access_token_client_id: str = Field(..., alias="accessTokenClientId")
    access_token_url: str = Field(..., alias="accessTokenUrl")
    access_token_client_secret: Optional[VaultSecret] = Field(
        ..., alias="accessTokenClientSecret"
    )
    blocked_versions: Optional[list[str]] = Field(..., alias="blockedVersions")
    inherit_version_data: Optional[
        list[OpenShiftClusterManagerV1_OpenShiftClusterManagerV1]
    ] = Field(..., alias="inheritVersionData")
    sectors: Optional[list[OpenShiftClusterManagerSectorV1]] = Field(
        ..., alias="sectors"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class AWSAccountV1(BaseModel):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    terraform_username: Optional[str] = Field(..., alias="terraformUsername")
    automation_token: VaultSecret = Field(..., alias="automationToken")

    class Config:
        smart_union = True
        extra = Extra.forbid


class UserV1(BaseModel):
    org_username: str = Field(..., alias="org_username")

    class Config:
        smart_union = True
        extra = Extra.forbid


class RoleV1(BaseModel):
    users: list[UserV1] = Field(..., alias="users")

    class Config:
        smart_union = True
        extra = Extra.forbid


class AWSGroupV1(BaseModel):
    account: AWSAccountV1 = Field(..., alias="account")
    roles: Optional[list[RoleV1]] = Field(..., alias="roles")

    class Config:
        smart_union = True
        extra = Extra.forbid


class AWSInfrastructureAccessV1(BaseModel):
    aws_group: AWSGroupV1 = Field(..., alias="awsGroup")
    access_level: str = Field(..., alias="accessLevel")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecAutoScaleV1(BaseModel):
    min_replicas: int = Field(..., alias="min_replicas")
    max_replicas: int = Field(..., alias="max_replicas")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecV1(BaseModel):
    product: str = Field(..., alias="product")
    hypershift: Optional[bool] = Field(..., alias="hypershift")
    q_id: Optional[str] = Field(..., alias="id")
    external_id: Optional[str] = Field(..., alias="external_id")
    provider: str = Field(..., alias="provider")
    region: str = Field(..., alias="region")
    channel: str = Field(..., alias="channel")
    version: str = Field(..., alias="version")
    initial_version: str = Field(..., alias="initial_version")
    multi_az: bool = Field(..., alias="multi_az")
    nodes: Optional[int] = Field(..., alias="nodes")
    instance_type: str = Field(..., alias="instance_type")
    private: bool = Field(..., alias="private")
    provision_shard_id: Optional[str] = Field(..., alias="provision_shard_id")
    autoscale: Optional[ClusterSpecAutoScaleV1] = Field(..., alias="autoscale")
    disable_user_workload_monitoring: Optional[bool] = Field(
        ..., alias="disable_user_workload_monitoring"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecOSDV1(ClusterSpecV1):
    storage: int = Field(..., alias="storage")
    load_balancers: int = Field(..., alias="load_balancers")

    class Config:
        smart_union = True
        extra = Extra.forbid


class RosaOcmAwsSpecV1_OpenShiftClusterManagerV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class RosaOcmAwsSpecV1(BaseModel):
    ocm: RosaOcmAwsSpecV1_OpenShiftClusterManagerV1 = Field(..., alias="ocm")
    creator_role_arn: str = Field(..., alias="creator_role_arn")
    installer_role_arn: str = Field(..., alias="installer_role_arn")
    support_role_arn: str = Field(..., alias="support_role_arn")
    controlplane_role_arn: str = Field(..., alias="controlplane_role_arn")
    worker_role_arn: str = Field(..., alias="worker_role_arn")

    class Config:
        smart_union = True
        extra = Extra.forbid


class RosaOcmSpecV1(BaseModel):
    ocm_environments: Optional[list[RosaOcmAwsSpecV1]] = Field(
        ..., alias="ocm_environments"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecROSAV1_AWSAccountV1(BaseModel):
    uid: str = Field(..., alias="uid")
    rosa: Optional[RosaOcmSpecV1] = Field(..., alias="rosa")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecROSAV1(ClusterSpecV1):
    subnet_ids: Optional[list[str]] = Field(..., alias="subnet_ids")
    availability_zones: Optional[list[str]] = Field(..., alias="availability_zones")
    account: Optional[ClusterSpecROSAV1_AWSAccountV1] = Field(..., alias="account")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterExternalConfigurationV1(BaseModel):
    labels: Json = Field(..., alias="labels")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterUpgradePolicyConditionsV1(BaseModel):
    soak_days: Optional[int] = Field(..., alias="soakDays")
    mutexes: Optional[list[str]] = Field(..., alias="mutexes")
    sector: Optional[str] = Field(..., alias="sector")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterUpgradePolicyV1(BaseModel):
    workloads: list[str] = Field(..., alias="workloads")
    schedule: str = Field(..., alias="schedule")
    conditions: ClusterUpgradePolicyConditionsV1 = Field(..., alias="conditions")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAdditionalRouterV1(BaseModel):
    private: bool = Field(..., alias="private")
    route_selectors: Optional[Json] = Field(..., alias="route_selectors")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterNetworkV1(BaseModel):
    q_type: Optional[str] = Field(..., alias="type")
    vpc: str = Field(..., alias="vpc")
    service: str = Field(..., alias="service")
    pod: str = Field(..., alias="pod")

    class Config:
        smart_union = True
        extra = Extra.forbid


class TaintV1(BaseModel):
    key: str = Field(..., alias="key")
    value: str = Field(..., alias="value")
    effect: str = Field(..., alias="effect")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterMachinePoolV1(BaseModel):
    q_id: str = Field(..., alias="id")
    instance_type: str = Field(..., alias="instance_type")
    replicas: int = Field(..., alias="replicas")
    labels: Optional[Json] = Field(..., alias="labels")
    taints: Optional[list[TaintV1]] = Field(..., alias="taints")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionV1(BaseModel):
    name: str = Field(..., alias="name")
    provider: str = Field(..., alias="provider")
    manage_routes: Optional[bool] = Field(..., alias="manageRoutes")
    delete: Optional[bool] = Field(..., alias="delete")

    class Config:
        smart_union = True
        extra = Extra.forbid


class AWSVPCV1_AWSAccountV1(BaseModel):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    terraform_username: Optional[str] = Field(..., alias="terraformUsername")
    automation_token: VaultSecret = Field(..., alias="automationToken")

    class Config:
        smart_union = True
        extra = Extra.forbid


class AWSVPCV1(BaseModel):
    account: AWSVPCV1_AWSAccountV1 = Field(..., alias="account")
    vpc_id: str = Field(..., alias="vpc_id")
    cidr_block: str = Field(..., alias="cidr_block")
    region: str = Field(..., alias="region")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionAccountV1(ClusterPeeringConnectionV1):
    vpc: AWSVPCV1 = Field(..., alias="vpc")
    assume_role: Optional[str] = Field(..., alias="assumeRole")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionAccountVPCMeshV1_AWSAccountV1(BaseModel):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    terraform_username: Optional[str] = Field(..., alias="terraformUsername")
    automation_token: VaultSecret = Field(..., alias="automationToken")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionAccountVPCMeshV1(ClusterPeeringConnectionV1):
    account: ClusterPeeringConnectionAccountVPCMeshV1_AWSAccountV1 = Field(
        ..., alias="account"
    )
    tags: Optional[Json] = Field(..., alias="tags")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionAccountTGWV1_AWSAccountV1(BaseModel):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    terraform_username: Optional[str] = Field(..., alias="terraformUsername")
    automation_token: VaultSecret = Field(..., alias="automationToken")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionAccountTGWV1(ClusterPeeringConnectionV1):
    account: ClusterPeeringConnectionAccountTGWV1_AWSAccountV1 = Field(
        ..., alias="account"
    )
    tags: Optional[Json] = Field(..., alias="tags")
    cidr_block: Optional[str] = Field(..., alias="cidrBlock")
    manage_security_groups: Optional[bool] = Field(..., alias="manageSecurityGroups")
    assume_role: Optional[str] = Field(..., alias="assumeRole")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterNetworkV1(BaseModel):
    vpc: str = Field(..., alias="vpc")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterSpecV1(BaseModel):
    region: str = Field(..., alias="region")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1_AWSInfrastructureAccessV1_AWSGroupV1_AWSAccountV1(
    BaseModel
):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    terraform_username: Optional[str] = Field(..., alias="terraformUsername")
    automation_token: VaultSecret = Field(..., alias="automationToken")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1_AWSInfrastructureAccessV1_AWSGroupV1(
    BaseModel
):
    account: ClusterPeeringConnectionClusterRequesterV1_ClusterV1_AWSInfrastructureAccessV1_AWSGroupV1_AWSAccountV1 = Field(
        ..., alias="account"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1_AWSInfrastructureAccessV1(
    BaseModel
):
    aws_group: ClusterPeeringConnectionClusterRequesterV1_ClusterV1_AWSInfrastructureAccessV1_AWSGroupV1 = Field(
        ..., alias="awsGroup"
    )
    access_level: str = Field(..., alias="accessLevel")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterPeeringV1_ClusterPeeringConnectionV1(
    BaseModel
):
    name: str = Field(..., alias="name")
    provider: str = Field(..., alias="provider")
    manage_routes: Optional[bool] = Field(..., alias="manageRoutes")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterAccepterV1_ClusterV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterAccepterV1_AWSAccountV1(BaseModel):
    name: str = Field(..., alias="name")
    uid: str = Field(..., alias="uid")
    terraform_username: Optional[str] = Field(..., alias="terraformUsername")
    automation_token: VaultSecret = Field(..., alias="automationToken")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterAccepterV1(
    ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterPeeringV1_ClusterPeeringConnectionV1
):
    name: str = Field(..., alias="name")
    cluster: ClusterPeeringConnectionClusterAccepterV1_ClusterV1 = Field(
        ..., alias="cluster"
    )
    aws_infrastructure_management_account: Optional[
        ClusterPeeringConnectionClusterAccepterV1_AWSAccountV1
    ] = Field(..., alias="awsInfrastructureManagementAccount")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterPeeringV1(BaseModel):
    connections: list[
        Union[
            ClusterPeeringConnectionClusterAccepterV1,
            ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterPeeringV1_ClusterPeeringConnectionV1,
        ]
    ] = Field(..., alias="connections")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1(BaseModel):
    name: str = Field(..., alias="name")
    network: Optional[
        ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterNetworkV1
    ] = Field(..., alias="network")
    spec: Optional[
        ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterSpecV1
    ] = Field(..., alias="spec")
    aws_infrastructure_access: Optional[
        list[
            ClusterPeeringConnectionClusterRequesterV1_ClusterV1_AWSInfrastructureAccessV1
        ]
    ] = Field(..., alias="awsInfrastructureAccess")
    aws_infrastructure_management_accounts: Optional[
        list[AWSInfrastructureManagementAccount]
    ] = Field(..., alias="awsInfrastructureManagementAccounts")
    peering: Optional[
        ClusterPeeringConnectionClusterRequesterV1_ClusterV1_ClusterPeeringV1
    ] = Field(..., alias="peering")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1(ClusterPeeringConnectionV1):
    cluster: ClusterPeeringConnectionClusterRequesterV1_ClusterV1 = Field(
        ..., alias="cluster"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringV1(BaseModel):
    connections: list[
        Union[
            ClusterPeeringConnectionAccountTGWV1,
            ClusterPeeringConnectionAccountV1,
            ClusterPeeringConnectionAccountVPCMeshV1,
            ClusterPeeringConnectionClusterRequesterV1,
            ClusterPeeringConnectionV1,
        ]
    ] = Field(..., alias="connections")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAddonParametersV1(BaseModel):
    q_id: str = Field(..., alias="id")
    value: str = Field(..., alias="value")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterAddonV1(BaseModel):
    name: str = Field(..., alias="name")
    parameters: Optional[list[ClusterAddonParametersV1]] = Field(
        ..., alias="parameters"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class DisableClusterAutomationsV1(BaseModel):
    e2e_tests: Optional[list[str]] = Field(..., alias="e2eTests")
    integrations: Optional[list[str]] = Field(..., alias="integrations")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterV1(BaseModel):
    path: str = Field(..., alias="path")
    name: str = Field(..., alias="name")
    server_url: str = Field(..., alias="serverUrl")
    console_url: str = Field(..., alias="consoleUrl")
    kibana_url: str = Field(..., alias="kibanaUrl")
    elb_fqdn: str = Field(..., alias="elbFQDN")
    prometheus_url: str = Field(..., alias="prometheusUrl")
    managed_groups: Optional[list[str]] = Field(..., alias="managedGroups")
    managed_cluster_roles: Optional[bool] = Field(..., alias="managedClusterRoles")
    insecure_skip_tls_verify: Optional[bool] = Field(..., alias="insecureSkipTLSVerify")
    jump_host: Optional[CommonJumphostFields] = Field(..., alias="jumpHost")
    auth: list[
        Union[ClusterAuthGithubOrgTeamV1, ClusterAuthGithubOrgV1, ClusterAuthV1]
    ] = Field(..., alias="auth")
    ocm: Optional[OpenShiftClusterManagerV1] = Field(..., alias="ocm")
    aws_infrastructure_access: Optional[list[AWSInfrastructureAccessV1]] = Field(
        ..., alias="awsInfrastructureAccess"
    )
    aws_infrastructure_management_accounts: Optional[
        list[AWSInfrastructureManagementAccount]
    ] = Field(..., alias="awsInfrastructureManagementAccounts")
    spec: Optional[Union[ClusterSpecROSAV1, ClusterSpecOSDV1, ClusterSpecV1]] = Field(
        ..., alias="spec"
    )
    external_configuration: Optional[ClusterExternalConfigurationV1] = Field(
        ..., alias="externalConfiguration"
    )
    upgrade_policy: Optional[ClusterUpgradePolicyV1] = Field(..., alias="upgradePolicy")
    additional_routers: Optional[list[ClusterAdditionalRouterV1]] = Field(
        ..., alias="additionalRouters"
    )
    network: Optional[ClusterNetworkV1] = Field(..., alias="network")
    machine_pools: Optional[list[ClusterMachinePoolV1]] = Field(
        ..., alias="machinePools"
    )
    peering: Optional[ClusterPeeringV1] = Field(..., alias="peering")
    addons: Optional[list[ClusterAddonV1]] = Field(..., alias="addons")
    automation_token: Optional[VaultSecret] = Field(..., alias="automationToken")
    cluster_admin: Optional[bool] = Field(..., alias="clusterAdmin")
    cluster_admin_automation_token: Optional[VaultSecret] = Field(
        ..., alias="clusterAdminAutomationToken"
    )
    internal: Optional[bool] = Field(..., alias="internal")
    disable: Optional[DisableClusterAutomationsV1] = Field(..., alias="disable")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClustersQueryData(BaseModel):
    clusters: Optional[list[ClusterV1]] = Field(..., alias="clusters")

    class Config:
        smart_union = True
        extra = Extra.forbid


def query(query_func: Callable, **kwargs: Any) -> ClustersQueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        ClustersQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return ClustersQueryData(**raw_data)
