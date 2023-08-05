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

from reconcile.gql_definitions.fragments.jumphost_common_fields import (
    CommonJumphostFields,
)
from reconcile.gql_definitions.fragments.vault_secret import VaultSecret


DEFINITION = """
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

query SkupperNetworks {
  skupper_networks: skupper_network_v1 {
    identifier
    siteConfigDefaults {
      clusterLocal
      console
      consoleAuthentication
      consoleIngress
      controllerCpuLimit
      controllerCpu
      controllerMemoryLimit
      controllerMemory
      controllerPodAntiaffinity
      controllerServiceAnnotations
      edge
      ingress
      routerConsole
      routerCpuLimit
      routerCpu
      routerMemoryLimit
      routerMemory
      routerLogging
      routerPodAntiaffinity
      routerServiceAnnotations
      routers
      serviceController
      serviceSync
      skupperSiteController
    }
    namespaces {
      name
      delete
      skupperSite {
        delete
        config {
          clusterLocal
          console
          consoleAuthentication
          consoleIngress
          controllerCpuLimit
          controllerCpu
          controllerMemoryLimit
          controllerMemory
          controllerPodAntiaffinity
          controllerServiceAnnotations
          edge
          ingress
          routerConsole
          routerCpuLimit
          routerCpu
          routerMemoryLimit
          routerMemory
          routerLogging
          routerPodAntiaffinity
          routerServiceAnnotations
          routers
          serviceController
          serviceSync
        }
      }
      cluster {
        name
        serverUrl
        insecureSkipTLSVerify
        jumpHost {
          ...CommonJumphostFields
        }
        spec {
          private
        }
        automationToken {
          ...VaultSecret
        }
        internal
        disable {
          integrations
        }
        peering {
          connections {
            provider
            ... on ClusterPeeringConnectionClusterRequester_v1 {
              cluster {
                name
              }
            }
            ... on ClusterPeeringConnectionClusterAccepter_v1 {
              cluster {
                name
              }
            }
          }
        }
      }
    }
  }
}
"""


class SkupperSiteConfigDefaultsV1(BaseModel):
    cluster_local: Optional[bool] = Field(..., alias="clusterLocal")
    console: Optional[bool] = Field(..., alias="console")
    console_authentication: Optional[str] = Field(..., alias="consoleAuthentication")
    console_ingress: Optional[str] = Field(..., alias="consoleIngress")
    controller_cpu_limit: Optional[str] = Field(..., alias="controllerCpuLimit")
    controller_cpu: Optional[str] = Field(..., alias="controllerCpu")
    controller_memory_limit: Optional[str] = Field(..., alias="controllerMemoryLimit")
    controller_memory: Optional[str] = Field(..., alias="controllerMemory")
    controller_pod_antiaffinity: Optional[str] = Field(
        ..., alias="controllerPodAntiaffinity"
    )
    controller_service_annotations: Optional[str] = Field(
        ..., alias="controllerServiceAnnotations"
    )
    edge: Optional[bool] = Field(..., alias="edge")
    ingress: Optional[str] = Field(..., alias="ingress")
    router_console: Optional[bool] = Field(..., alias="routerConsole")
    router_cpu_limit: Optional[str] = Field(..., alias="routerCpuLimit")
    router_cpu: Optional[str] = Field(..., alias="routerCpu")
    router_memory_limit: Optional[str] = Field(..., alias="routerMemoryLimit")
    router_memory: Optional[str] = Field(..., alias="routerMemory")
    router_logging: Optional[str] = Field(..., alias="routerLogging")
    router_pod_antiaffinity: Optional[str] = Field(..., alias="routerPodAntiaffinity")
    router_service_annotations: Optional[str] = Field(
        ..., alias="routerServiceAnnotations"
    )
    routers: Optional[int] = Field(..., alias="routers")
    service_controller: Optional[bool] = Field(..., alias="serviceController")
    service_sync: Optional[bool] = Field(..., alias="serviceSync")
    skupper_site_controller: str = Field(..., alias="skupperSiteController")

    class Config:
        smart_union = True
        extra = Extra.forbid


class SkupperSiteConfigV1(BaseModel):
    cluster_local: Optional[bool] = Field(..., alias="clusterLocal")
    console: Optional[bool] = Field(..., alias="console")
    console_authentication: Optional[str] = Field(..., alias="consoleAuthentication")
    console_ingress: Optional[str] = Field(..., alias="consoleIngress")
    controller_cpu_limit: Optional[str] = Field(..., alias="controllerCpuLimit")
    controller_cpu: Optional[str] = Field(..., alias="controllerCpu")
    controller_memory_limit: Optional[str] = Field(..., alias="controllerMemoryLimit")
    controller_memory: Optional[str] = Field(..., alias="controllerMemory")
    controller_pod_antiaffinity: Optional[str] = Field(
        ..., alias="controllerPodAntiaffinity"
    )
    controller_service_annotations: Optional[str] = Field(
        ..., alias="controllerServiceAnnotations"
    )
    edge: Optional[bool] = Field(..., alias="edge")
    ingress: Optional[str] = Field(..., alias="ingress")
    router_console: Optional[bool] = Field(..., alias="routerConsole")
    router_cpu_limit: Optional[str] = Field(..., alias="routerCpuLimit")
    router_cpu: Optional[str] = Field(..., alias="routerCpu")
    router_memory_limit: Optional[str] = Field(..., alias="routerMemoryLimit")
    router_memory: Optional[str] = Field(..., alias="routerMemory")
    router_logging: Optional[str] = Field(..., alias="routerLogging")
    router_pod_antiaffinity: Optional[str] = Field(..., alias="routerPodAntiaffinity")
    router_service_annotations: Optional[str] = Field(
        ..., alias="routerServiceAnnotations"
    )
    routers: Optional[int] = Field(..., alias="routers")
    service_controller: Optional[bool] = Field(..., alias="serviceController")
    service_sync: Optional[bool] = Field(..., alias="serviceSync")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceSkupperSiteConfigV1(BaseModel):
    delete: Optional[bool] = Field(..., alias="delete")
    config: Optional[SkupperSiteConfigV1] = Field(..., alias="config")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterSpecV1(BaseModel):
    private: bool = Field(..., alias="private")

    class Config:
        smart_union = True
        extra = Extra.forbid


class DisableClusterAutomationsV1(BaseModel):
    integrations: Optional[list[str]] = Field(..., alias="integrations")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionV1(BaseModel):
    provider: str = Field(..., alias="provider")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterRequesterV1_ClusterV1(BaseModel):
    name: str = Field(..., alias="name")

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


class ClusterPeeringConnectionClusterAccepterV1_ClusterV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringConnectionClusterAccepterV1(ClusterPeeringConnectionV1):
    cluster: ClusterPeeringConnectionClusterAccepterV1_ClusterV1 = Field(
        ..., alias="cluster"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterPeeringV1(BaseModel):
    connections: list[
        Union[
            ClusterPeeringConnectionClusterRequesterV1,
            ClusterPeeringConnectionClusterAccepterV1,
            ClusterPeeringConnectionV1,
        ]
    ] = Field(..., alias="connections")

    class Config:
        smart_union = True
        extra = Extra.forbid


class ClusterV1(BaseModel):
    name: str = Field(..., alias="name")
    server_url: str = Field(..., alias="serverUrl")
    insecure_skip_tls_verify: Optional[bool] = Field(..., alias="insecureSkipTLSVerify")
    jump_host: Optional[CommonJumphostFields] = Field(..., alias="jumpHost")
    spec: Optional[ClusterSpecV1] = Field(..., alias="spec")
    automation_token: Optional[VaultSecret] = Field(..., alias="automationToken")
    internal: Optional[bool] = Field(..., alias="internal")
    disable: Optional[DisableClusterAutomationsV1] = Field(..., alias="disable")
    peering: Optional[ClusterPeeringV1] = Field(..., alias="peering")

    class Config:
        smart_union = True
        extra = Extra.forbid


class NamespaceV1(BaseModel):
    name: str = Field(..., alias="name")
    delete: Optional[bool] = Field(..., alias="delete")
    skupper_site: Optional[NamespaceSkupperSiteConfigV1] = Field(
        ..., alias="skupperSite"
    )
    cluster: ClusterV1 = Field(..., alias="cluster")

    class Config:
        smart_union = True
        extra = Extra.forbid


class SkupperNetworkV1(BaseModel):
    identifier: str = Field(..., alias="identifier")
    site_config_defaults: SkupperSiteConfigDefaultsV1 = Field(
        ..., alias="siteConfigDefaults"
    )
    namespaces: list[NamespaceV1] = Field(..., alias="namespaces")

    class Config:
        smart_union = True
        extra = Extra.forbid


class SkupperNetworksQueryData(BaseModel):
    skupper_networks: Optional[list[SkupperNetworkV1]] = Field(
        ..., alias="skupper_networks"
    )

    class Config:
        smart_union = True
        extra = Extra.forbid


def query(query_func: Callable, **kwargs: Any) -> SkupperNetworksQueryData:
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
        SkupperNetworksQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return SkupperNetworksQueryData(**raw_data)
