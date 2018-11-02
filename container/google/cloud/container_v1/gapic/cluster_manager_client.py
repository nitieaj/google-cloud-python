# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Accesses the google.container.v1 ClusterManager API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.grpc_helpers
import google.api_core.path_template
import grpc

from google.cloud.container_v1.gapic import cluster_manager_client_config
from google.cloud.container_v1.gapic import enums
from google.cloud.container_v1.gapic.transports import cluster_manager_grpc_transport
from google.cloud.container_v1.proto import cluster_service_pb2
from google.cloud.container_v1.proto import cluster_service_pb2_grpc
from google.protobuf import empty_pb2

_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-container', ).version


class ClusterManagerClient(object):
    """Google Kubernetes Engine Cluster Manager v1"""

    SERVICE_ADDRESS = 'container.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.container.v1.ClusterManager'

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ClusterManagerClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            'projects/{project}/locations/{location}',
            project=project,
            location=location,
        )

    @classmethod
    def cluster_path(cls, project, location, cluster):
        """Return a fully-qualified cluster string."""
        return google.api_core.path_template.expand(
            'projects/{project}/locations/{location}/clusters/{cluster}',
            project=project,
            location=location,
            cluster=cluster,
        )

    @classmethod
    def node_pool_path(cls, project, location, cluster, node_pool):
        """Return a fully-qualified node_pool string."""
        return google.api_core.path_template.expand(
            'projects/{project}/locations/{location}/clusters/{cluster}/nodePools/{node_pool}',
            project=project,
            location=location,
            cluster=cluster,
            node_pool=node_pool,
        )

    @classmethod
    def operation_path(cls, project, location, operation_):
        """Return a fully-qualified operation string."""
        return google.api_core.path_template.expand(
            'projects/{project}/locations/{location}/operations/{operation}',
            project=project,
            location=location,
            operation=operation_,
        )

    def __init__(self,
                 transport=None,
                 channel=None,
                 credentials=None,
                 client_config=cluster_manager_client_config.config,
                 client_info=None):
        """Constructor.

        Args:
            transport (Union[~.ClusterManagerGrpcTransport,
                    Callable[[~.Credentials, type], ~.ClusterManagerGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config:
            warnings.warn('The `client_config` argument is deprecated.',
                          PendingDeprecationWarning)
        if channel:
            warnings.warn(
                'The `channel` argument is deprecated; use '
                '`transport` instead.', PendingDeprecationWarning)

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=cluster_manager_grpc_transport.
                    ClusterManagerGrpcTransport,
                )
            else:
                if credentials:
                    raise ValueError(
                        'Received both a transport instance and '
                        'credentials; these are mutually exclusive.')
                self.transport = transport
        else:
            self.transport = cluster_manager_grpc_transport.ClusterManagerGrpcTransport(
                address=self.SERVICE_ADDRESS,
                channel=channel,
                credentials=credentials,
            )

        if client_info is None:
            client_info = (
                google.api_core.gapic_v1.client_info.DEFAULT_CLIENT_INFO)
        client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME], )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_clusters(self,
                      parent,
                      project_id=None,
                      zone=None,
                      retry=google.api_core.gapic_v1.method.DEFAULT,
                      timeout=google.api_core.gapic_v1.method.DEFAULT,
                      metadata=None):
        """
        Lists all clusters owned by a project in either the specified zone or all
        zones.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.list_clusters(parent)

        Args:
            parent (str): The parent (project and location) where the clusters will be listed.
                Specified in the format 'projects/*/locations/*'.
                Location \"-\" matches all zones and all regions.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the parent field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides, or \"-\" for all zones.
                This field has been deprecated and replaced by the parent field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ListClustersResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_clusters' not in self._inner_api_calls:
            self._inner_api_calls[
                'list_clusters'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.list_clusters,
                    default_retry=self._method_configs['ListClusters'].retry,
                    default_timeout=self._method_configs['ListClusters'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.ListClustersRequest(
            parent=parent,
            project_id=project_id,
            zone=zone,
        )
        return self._inner_api_calls['list_clusters'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def get_cluster(self,
                    name,
                    project_id=None,
                    zone=None,
                    cluster_id=None,
                    retry=google.api_core.gapic_v1.method.DEFAULT,
                    timeout=google.api_core.gapic_v1.method.DEFAULT,
                    metadata=None):
        """
        Gets the details of a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.get_cluster(name)

        Args:
            name (str): The name (project, location, cluster) of the cluster to retrieve.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to retrieve.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Cluster` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_cluster' not in self._inner_api_calls:
            self._inner_api_calls[
                'get_cluster'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.get_cluster,
                    default_retry=self._method_configs['GetCluster'].retry,
                    default_timeout=self._method_configs['GetCluster'].timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.GetClusterRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['get_cluster'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def create_cluster(self,
                       cluster,
                       parent,
                       project_id=None,
                       zone=None,
                       retry=google.api_core.gapic_v1.method.DEFAULT,
                       timeout=google.api_core.gapic_v1.method.DEFAULT,
                       metadata=None):
        """
        Creates a cluster, consisting of the specified number and type of Google
        Compute Engine instances.

        By default, the cluster is created in the project's
        `default network <https://cloud.google.com/compute/docs/networks-and-firewalls#networks>`_.

        One firewall is added for the cluster. After cluster creation,
        the cluster creates routes for each node to allow the containers
        on that node to communicate with all other instances in the
        cluster.

        Finally, an entry is added to the project's global metadata indicating
        which CIDR range is being used by the cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``cluster``:
            >>> cluster = {}
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.create_cluster(cluster, parent)

        Args:
            cluster (Union[dict, ~google.cloud.container_v1.types.Cluster]): A [cluster
                resource](/container-engine/reference/rest/v1/projects.zones.clusters)
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.Cluster`
            parent (str): The parent (project and location) where the cluster will be created.
                Specified in the format 'projects/*/locations/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the parent field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the parent field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_cluster' not in self._inner_api_calls:
            self._inner_api_calls[
                'create_cluster'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.create_cluster,
                    default_retry=self._method_configs['CreateCluster'].retry,
                    default_timeout=self._method_configs['CreateCluster'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.CreateClusterRequest(
            cluster=cluster,
            parent=parent,
            project_id=project_id,
            zone=zone,
        )
        return self._inner_api_calls['create_cluster'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def update_cluster(self,
                       update,
                       name,
                       project_id=None,
                       zone=None,
                       cluster_id=None,
                       retry=google.api_core.gapic_v1.method.DEFAULT,
                       timeout=google.api_core.gapic_v1.method.DEFAULT,
                       metadata=None):
        """
        Updates the settings of a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``update``:
            >>> update = {}
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.update_cluster(update, name)

        Args:
            update (Union[dict, ~google.cloud.container_v1.types.ClusterUpdate]): A description of the update.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.ClusterUpdate`
            name (str): The name (project, location, cluster) of the cluster to update.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_cluster' not in self._inner_api_calls:
            self._inner_api_calls[
                'update_cluster'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.update_cluster,
                    default_retry=self._method_configs['UpdateCluster'].retry,
                    default_timeout=self._method_configs['UpdateCluster'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.UpdateClusterRequest(
            update=update,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['update_cluster'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def update_node_pool(self,
                         node_version,
                         image_type,
                         name,
                         project_id=None,
                         zone=None,
                         cluster_id=None,
                         node_pool_id=None,
                         retry=google.api_core.gapic_v1.method.DEFAULT,
                         timeout=google.api_core.gapic_v1.method.DEFAULT,
                         metadata=None):
        """
        Updates the version and/or image type for a specific node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``node_version``:
            >>> node_version = ''
            >>>
            >>> # TODO: Initialize ``image_type``:
            >>> image_type = ''
            >>> name = client.node_pool_path('[PROJECT]', '[LOCATION]', '[CLUSTER]', '[NODE_POOL]')
            >>>
            >>> response = client.update_node_pool(node_version, image_type, name)

        Args:
            node_version (str): The Kubernetes version to change the nodes to (typically an
                upgrade).

                Users may specify either explicit versions offered by Kubernetes Engine or
                version aliases, which have the following behavior:

                - \"latest\": picks the highest valid Kubernetes version
                - \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version
                - \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version
                - \"1.X.Y-gke.N\": picks an explicit Kubernetes version
                - \"-\": picks the Kubernetes master version
            image_type (str): The desired image type for the node pool.
            name (str): The name (project, location, cluster, node pool) of the node pool to
                update. Specified in the format
                'projects/*/locations/*/clusters/*/nodePools/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_node_pool' not in self._inner_api_calls:
            self._inner_api_calls[
                'update_node_pool'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.update_node_pool,
                    default_retry=self._method_configs['UpdateNodePool'].retry,
                    default_timeout=self._method_configs['UpdateNodePool'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.UpdateNodePoolRequest(
            node_version=node_version,
            image_type=image_type,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
        )
        return self._inner_api_calls['update_node_pool'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_node_pool_autoscaling(
            self,
            autoscaling,
            name,
            project_id=None,
            zone=None,
            cluster_id=None,
            node_pool_id=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Sets the autoscaling settings for a specific node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``autoscaling``:
            >>> autoscaling = {}
            >>> name = client.node_pool_path('[PROJECT]', '[LOCATION]', '[CLUSTER]', '[NODE_POOL]')
            >>>
            >>> response = client.set_node_pool_autoscaling(autoscaling, name)

        Args:
            autoscaling (Union[dict, ~google.cloud.container_v1.types.NodePoolAutoscaling]): Autoscaling configuration for the node pool.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NodePoolAutoscaling`
            name (str): The name (project, location, cluster, node pool) of the node pool to set
                autoscaler settings. Specified in the format
                'projects/*/locations/*/clusters/*/nodePools/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_node_pool_autoscaling' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_node_pool_autoscaling'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_node_pool_autoscaling,
                    default_retry=self.
                    _method_configs['SetNodePoolAutoscaling'].retry,
                    default_timeout=self.
                    _method_configs['SetNodePoolAutoscaling'].timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetNodePoolAutoscalingRequest(
            autoscaling=autoscaling,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
        )
        return self._inner_api_calls['set_node_pool_autoscaling'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_logging_service(self,
                            logging_service,
                            name,
                            project_id=None,
                            zone=None,
                            cluster_id=None,
                            retry=google.api_core.gapic_v1.method.DEFAULT,
                            timeout=google.api_core.gapic_v1.method.DEFAULT,
                            metadata=None):
        """
        Sets the logging service for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``logging_service``:
            >>> logging_service = ''
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_logging_service(logging_service, name)

        Args:
            logging_service (str): The logging service the cluster should use to write metrics.
                Currently available options:

                * \"logging.googleapis.com\" - the Google Cloud Logging service
                * \"none\" - no metrics will be exported from the cluster
            name (str): The name (project, location, cluster) of the cluster to set logging.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_logging_service' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_logging_service'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_logging_service,
                    default_retry=self._method_configs['SetLoggingService'].
                    retry,
                    default_timeout=self._method_configs['SetLoggingService'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetLoggingServiceRequest(
            logging_service=logging_service,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_logging_service'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_monitoring_service(self,
                               monitoring_service,
                               name,
                               project_id=None,
                               zone=None,
                               cluster_id=None,
                               retry=google.api_core.gapic_v1.method.DEFAULT,
                               timeout=google.api_core.gapic_v1.method.DEFAULT,
                               metadata=None):
        """
        Sets the monitoring service for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``monitoring_service``:
            >>> monitoring_service = ''
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_monitoring_service(monitoring_service, name)

        Args:
            monitoring_service (str): The monitoring service the cluster should use to write metrics.
                Currently available options:

                * \"monitoring.googleapis.com\" - the Google Cloud Monitoring service
                * \"none\" - no metrics will be exported from the cluster
            name (str): The name (project, location, cluster) of the cluster to set monitoring.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_monitoring_service' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_monitoring_service'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_monitoring_service,
                    default_retry=self._method_configs['SetMonitoringService'].
                    retry,
                    default_timeout=self.
                    _method_configs['SetMonitoringService'].timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetMonitoringServiceRequest(
            monitoring_service=monitoring_service,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_monitoring_service'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_addons_config(self,
                          addons_config,
                          name,
                          project_id=None,
                          zone=None,
                          cluster_id=None,
                          retry=google.api_core.gapic_v1.method.DEFAULT,
                          timeout=google.api_core.gapic_v1.method.DEFAULT,
                          metadata=None):
        """
        Sets the addons for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``addons_config``:
            >>> addons_config = {}
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_addons_config(addons_config, name)

        Args:
            addons_config (Union[dict, ~google.cloud.container_v1.types.AddonsConfig]): The desired configurations for the various addons available to run in the
                cluster.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.AddonsConfig`
            name (str): The name (project, location, cluster) of the cluster to set addons.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_addons_config' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_addons_config'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_addons_config,
                    default_retry=self._method_configs['SetAddonsConfig'].
                    retry,
                    default_timeout=self._method_configs['SetAddonsConfig'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetAddonsConfigRequest(
            addons_config=addons_config,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_addons_config'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_locations(self,
                      locations,
                      name,
                      project_id=None,
                      zone=None,
                      cluster_id=None,
                      retry=google.api_core.gapic_v1.method.DEFAULT,
                      timeout=google.api_core.gapic_v1.method.DEFAULT,
                      metadata=None):
        """
        Sets the locations for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``locations``:
            >>> locations = []
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_locations(locations, name)

        Args:
            locations (list[str]): The desired list of Google Compute Engine
                `locations <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster's nodes
                should be located. Changing the locations a cluster is in will result
                in nodes being either created or removed from the cluster, depending on
                whether locations are being added or removed.

                This list must always include the cluster's primary zone.
            name (str): The name (project, location, cluster) of the cluster to set locations.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_locations' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_locations'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_locations,
                    default_retry=self._method_configs['SetLocations'].retry,
                    default_timeout=self._method_configs['SetLocations'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetLocationsRequest(
            locations=locations,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_locations'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def update_master(self,
                      master_version,
                      name,
                      project_id=None,
                      zone=None,
                      cluster_id=None,
                      retry=google.api_core.gapic_v1.method.DEFAULT,
                      timeout=google.api_core.gapic_v1.method.DEFAULT,
                      metadata=None):
        """
        Updates the master for a specific cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``master_version``:
            >>> master_version = ''
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.update_master(master_version, name)

        Args:
            master_version (str): The Kubernetes version to change the master to.

                Users may specify either explicit versions offered by Kubernetes Engine or
                version aliases, which have the following behavior:

                - \"latest\": picks the highest valid Kubernetes version
                - \"1.X\": picks the highest valid patch+gke.N patch in the 1.X version
                - \"1.X.Y\": picks the highest valid gke.N patch in the 1.X.Y version
                - \"1.X.Y-gke.N\": picks an explicit Kubernetes version
                - \"-\": picks the default Kubernetes version
            name (str): The name (project, location, cluster) of the cluster to update.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_master' not in self._inner_api_calls:
            self._inner_api_calls[
                'update_master'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.update_master,
                    default_retry=self._method_configs['UpdateMaster'].retry,
                    default_timeout=self._method_configs['UpdateMaster'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.UpdateMasterRequest(
            master_version=master_version,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['update_master'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_master_auth(self,
                        action,
                        update,
                        name,
                        project_id=None,
                        zone=None,
                        cluster_id=None,
                        retry=google.api_core.gapic_v1.method.DEFAULT,
                        timeout=google.api_core.gapic_v1.method.DEFAULT,
                        metadata=None):
        """
        Used to set master auth materials. Currently supports :-
        Changing the admin password for a specific cluster.
        This can be either via password generation or explicitly set the password.

        Example:
            >>> from google.cloud import container_v1
            >>> from google.cloud.container_v1 import enums
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``action``:
            >>> action = enums.SetMasterAuthRequest.Action.UNKNOWN
            >>>
            >>> # TODO: Initialize ``update``:
            >>> update = {}
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_master_auth(action, update, name)

        Args:
            action (~google.cloud.container_v1.types.Action): The exact form of action to be taken on the master auth.
            update (Union[dict, ~google.cloud.container_v1.types.MasterAuth]): A description of the update.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.MasterAuth`
            name (str): The name (project, location, cluster) of the cluster to set auth.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to upgrade.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_master_auth' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_master_auth'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_master_auth,
                    default_retry=self._method_configs['SetMasterAuth'].retry,
                    default_timeout=self._method_configs['SetMasterAuth'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetMasterAuthRequest(
            action=action,
            update=update,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_master_auth'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_cluster(self,
                       name,
                       project_id=None,
                       zone=None,
                       cluster_id=None,
                       retry=google.api_core.gapic_v1.method.DEFAULT,
                       timeout=google.api_core.gapic_v1.method.DEFAULT,
                       metadata=None):
        """
        Deletes the cluster, including the Kubernetes endpoint and all worker
        nodes.

        Firewalls and routes that were configured during cluster creation
        are also deleted.

        Other Google Compute Engine resources that might be in use by the cluster
        (e.g. load balancer resources) will not be deleted if they weren't present
        at the initial create time.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.delete_cluster(name)

        Args:
            name (str): The name (project, location, cluster) of the cluster to delete.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to delete.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_cluster' not in self._inner_api_calls:
            self._inner_api_calls[
                'delete_cluster'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.delete_cluster,
                    default_retry=self._method_configs['DeleteCluster'].retry,
                    default_timeout=self._method_configs['DeleteCluster'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.DeleteClusterRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['delete_cluster'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def list_operations(self,
                        parent,
                        project_id=None,
                        zone=None,
                        retry=google.api_core.gapic_v1.method.DEFAULT,
                        timeout=google.api_core.gapic_v1.method.DEFAULT,
                        metadata=None):
        """
        Lists all operations in a project in a specific zone or all zones.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.list_operations(parent)

        Args:
            parent (str): The parent (project and location) where the operations will be listed.
                Specified in the format 'projects/*/locations/*'.
                Location \"-\" matches all zones and all regions.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the parent field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ to return operations for, or ``-`` for
                all zones. This field has been deprecated and replaced by the parent field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ListOperationsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_operations' not in self._inner_api_calls:
            self._inner_api_calls[
                'list_operations'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.list_operations,
                    default_retry=self._method_configs['ListOperations'].retry,
                    default_timeout=self._method_configs['ListOperations'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.ListOperationsRequest(
            parent=parent,
            project_id=project_id,
            zone=zone,
        )
        return self._inner_api_calls['list_operations'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def get_operation(self,
                      name,
                      project_id=None,
                      zone=None,
                      operation_id=None,
                      retry=google.api_core.gapic_v1.method.DEFAULT,
                      timeout=google.api_core.gapic_v1.method.DEFAULT,
                      metadata=None):
        """
        Gets the specified operation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.operation_path('[PROJECT]', '[LOCATION]', '[OPERATION]')
            >>>
            >>> response = client.get_operation(name)

        Args:
            name (str): The name (project, location, operation id) of the operation to get.
                Specified in the format 'projects/*/locations/*/operations/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            operation_id (str): Deprecated. The server-assigned ``name`` of the operation.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_operation' not in self._inner_api_calls:
            self._inner_api_calls[
                'get_operation'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.get_operation,
                    default_retry=self._method_configs['GetOperation'].retry,
                    default_timeout=self._method_configs['GetOperation'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.GetOperationRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            operation_id=operation_id,
        )
        return self._inner_api_calls['get_operation'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def cancel_operation(self,
                         name,
                         project_id=None,
                         zone=None,
                         operation_id=None,
                         retry=google.api_core.gapic_v1.method.DEFAULT,
                         timeout=google.api_core.gapic_v1.method.DEFAULT,
                         metadata=None):
        """
        Cancels the specified operation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.operation_path('[PROJECT]', '[LOCATION]', '[OPERATION]')
            >>>
            >>> client.cancel_operation(name)

        Args:
            name (str): The name (project, location, operation id) of the operation to cancel.
                Specified in the format 'projects/*/locations/*/operations/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the operation resides.
                This field has been deprecated and replaced by the name field.
            operation_id (str): Deprecated. The server-assigned ``name`` of the operation.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'cancel_operation' not in self._inner_api_calls:
            self._inner_api_calls[
                'cancel_operation'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.cancel_operation,
                    default_retry=self._method_configs['CancelOperation'].
                    retry,
                    default_timeout=self._method_configs['CancelOperation'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.CancelOperationRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            operation_id=operation_id,
        )
        self._inner_api_calls['cancel_operation'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def get_server_config(self,
                          name,
                          project_id=None,
                          zone=None,
                          retry=google.api_core.gapic_v1.method.DEFAULT,
                          timeout=google.api_core.gapic_v1.method.DEFAULT,
                          metadata=None):
        """
        Returns configuration info about the Kubernetes Engine service.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> response = client.get_server_config(name)

        Args:
            name (str): The name (project and location) of the server config to get
                Specified in the format 'projects/*/locations/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ to return operations for.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ServerConfig` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_server_config' not in self._inner_api_calls:
            self._inner_api_calls[
                'get_server_config'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.get_server_config,
                    default_retry=self._method_configs['GetServerConfig'].
                    retry,
                    default_timeout=self._method_configs['GetServerConfig'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.GetServerConfigRequest(
            name=name,
            project_id=project_id,
            zone=zone,
        )
        return self._inner_api_calls['get_server_config'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def list_node_pools(self,
                        parent,
                        project_id=None,
                        zone=None,
                        cluster_id=None,
                        retry=google.api_core.gapic_v1.method.DEFAULT,
                        timeout=google.api_core.gapic_v1.method.DEFAULT,
                        metadata=None):
        """
        Lists the node pools for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> parent = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.list_node_pools(parent)

        Args:
            parent (str): The parent (project, location, cluster id) where the node pools will be
                listed. Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the parent field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the parent field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the parent field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.ListNodePoolsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_node_pools' not in self._inner_api_calls:
            self._inner_api_calls[
                'list_node_pools'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.list_node_pools,
                    default_retry=self._method_configs['ListNodePools'].retry,
                    default_timeout=self._method_configs['ListNodePools'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.ListNodePoolsRequest(
            parent=parent,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['list_node_pools'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def get_node_pool(self,
                      name,
                      project_id=None,
                      zone=None,
                      cluster_id=None,
                      node_pool_id=None,
                      retry=google.api_core.gapic_v1.method.DEFAULT,
                      timeout=google.api_core.gapic_v1.method.DEFAULT,
                      metadata=None):
        """
        Retrieves the node pool requested.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.node_pool_path('[PROJECT]', '[LOCATION]', '[CLUSTER]', '[NODE_POOL]')
            >>>
            >>> response = client.get_node_pool(name)

        Args:
            name (str): The name (project, location, cluster, node pool id) of the node pool to
                get. Specified in the format
                'projects/*/locations/*/clusters/*/nodePools/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.NodePool` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_node_pool' not in self._inner_api_calls:
            self._inner_api_calls[
                'get_node_pool'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.get_node_pool,
                    default_retry=self._method_configs['GetNodePool'].retry,
                    default_timeout=self._method_configs['GetNodePool'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.GetNodePoolRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
        )
        return self._inner_api_calls['get_node_pool'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def create_node_pool(self,
                         node_pool,
                         parent,
                         project_id=None,
                         zone=None,
                         cluster_id=None,
                         retry=google.api_core.gapic_v1.method.DEFAULT,
                         timeout=google.api_core.gapic_v1.method.DEFAULT,
                         metadata=None):
        """
        Creates a node pool for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``node_pool``:
            >>> node_pool = {}
            >>> parent = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.create_node_pool(node_pool, parent)

        Args:
            node_pool (Union[dict, ~google.cloud.container_v1.types.NodePool]): The node pool to create.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NodePool`
            parent (str): The parent (project, location, cluster id) where the node pool will be
                created. Specified in the format
                'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the parent field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the parent field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the parent field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_node_pool' not in self._inner_api_calls:
            self._inner_api_calls[
                'create_node_pool'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.create_node_pool,
                    default_retry=self._method_configs['CreateNodePool'].retry,
                    default_timeout=self._method_configs['CreateNodePool'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.CreateNodePoolRequest(
            node_pool=node_pool,
            parent=parent,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['create_node_pool'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_node_pool(self,
                         name,
                         project_id=None,
                         zone=None,
                         cluster_id=None,
                         node_pool_id=None,
                         retry=google.api_core.gapic_v1.method.DEFAULT,
                         timeout=google.api_core.gapic_v1.method.DEFAULT,
                         metadata=None):
        """
        Deletes a node pool from a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.node_pool_path('[PROJECT]', '[LOCATION]', '[CLUSTER]', '[NODE_POOL]')
            >>>
            >>> response = client.delete_node_pool(name)

        Args:
            name (str): The name (project, location, cluster, node pool id) of the node pool to
                delete. Specified in the format
                'projects/*/locations/*/clusters/*/nodePools/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to delete.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_node_pool' not in self._inner_api_calls:
            self._inner_api_calls[
                'delete_node_pool'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.delete_node_pool,
                    default_retry=self._method_configs['DeleteNodePool'].retry,
                    default_timeout=self._method_configs['DeleteNodePool'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.DeleteNodePoolRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
        )
        return self._inner_api_calls['delete_node_pool'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def rollback_node_pool_upgrade(
            self,
            name,
            project_id=None,
            zone=None,
            cluster_id=None,
            node_pool_id=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Roll back the previously Aborted or Failed NodePool upgrade.
        This will be an no-op if the last upgrade successfully completed.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.node_pool_path('[PROJECT]', '[LOCATION]', '[CLUSTER]', '[NODE_POOL]')
            >>>
            >>> response = client.rollback_node_pool_upgrade(name)

        Args:
            name (str): The name (project, location, cluster, node pool id) of the node poll to
                rollback upgrade.
                Specified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to rollback.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to rollback.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'rollback_node_pool_upgrade' not in self._inner_api_calls:
            self._inner_api_calls[
                'rollback_node_pool_upgrade'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.rollback_node_pool_upgrade,
                    default_retry=self.
                    _method_configs['RollbackNodePoolUpgrade'].retry,
                    default_timeout=self.
                    _method_configs['RollbackNodePoolUpgrade'].timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.RollbackNodePoolUpgradeRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
        )
        return self._inner_api_calls['rollback_node_pool_upgrade'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_node_pool_management(
            self,
            management,
            name,
            project_id=None,
            zone=None,
            cluster_id=None,
            node_pool_id=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Sets the NodeManagement options for a node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``management``:
            >>> management = {}
            >>> name = client.node_pool_path('[PROJECT]', '[LOCATION]', '[CLUSTER]', '[NODE_POOL]')
            >>>
            >>> response = client.set_node_pool_management(management, name)

        Args:
            management (Union[dict, ~google.cloud.container_v1.types.NodeManagement]): NodeManagement configuration for the node pool.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NodeManagement`
            name (str): The name (project, location, cluster, node pool id) of the node pool to set
                management properties. Specified in the format
                'projects/*/locations/*/clusters/*/nodePools/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to update.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to update.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_node_pool_management' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_node_pool_management'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_node_pool_management,
                    default_retry=self.
                    _method_configs['SetNodePoolManagement'].retry,
                    default_timeout=self.
                    _method_configs['SetNodePoolManagement'].timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetNodePoolManagementRequest(
            management=management,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
        )
        return self._inner_api_calls['set_node_pool_management'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_labels(self,
                   resource_labels,
                   label_fingerprint,
                   name,
                   project_id=None,
                   zone=None,
                   cluster_id=None,
                   retry=google.api_core.gapic_v1.method.DEFAULT,
                   timeout=google.api_core.gapic_v1.method.DEFAULT,
                   metadata=None):
        """
        Sets labels on a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``resource_labels``:
            >>> resource_labels = {}
            >>>
            >>> # TODO: Initialize ``label_fingerprint``:
            >>> label_fingerprint = ''
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_labels(resource_labels, label_fingerprint, name)

        Args:
            resource_labels (dict[str -> str]): The labels to set for that cluster.
            label_fingerprint (str): The fingerprint of the previous set of labels for this resource,
                used to detect conflicts. The fingerprint is initially generated by
                Kubernetes Engine and changes after every request to modify or update
                labels. You must always provide an up-to-date fingerprint hash when
                updating or changing labels. Make a <code>get()</code> request to the
                resource to get the latest fingerprint.
            name (str): The name (project, location, cluster id) of the cluster to set labels.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_labels' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_labels'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_labels,
                    default_retry=self._method_configs['SetLabels'].retry,
                    default_timeout=self._method_configs['SetLabels'].timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetLabelsRequest(
            resource_labels=resource_labels,
            label_fingerprint=label_fingerprint,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_labels'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_legacy_abac(self,
                        enabled,
                        name,
                        project_id=None,
                        zone=None,
                        cluster_id=None,
                        retry=google.api_core.gapic_v1.method.DEFAULT,
                        timeout=google.api_core.gapic_v1.method.DEFAULT,
                        metadata=None):
        """
        Enables or disables the ABAC authorization mechanism on a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``enabled``:
            >>> enabled = False
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_legacy_abac(enabled, name)

        Args:
            enabled (bool): Whether ABAC authorization will be enabled in the cluster.
            name (str): The name (project, location, cluster id) of the cluster to set legacy abac.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to update.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_legacy_abac' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_legacy_abac'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_legacy_abac,
                    default_retry=self._method_configs['SetLegacyAbac'].retry,
                    default_timeout=self._method_configs['SetLegacyAbac'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetLegacyAbacRequest(
            enabled=enabled,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_legacy_abac'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def start_i_p_rotation(self,
                           name,
                           rotate_credentials,
                           project_id=None,
                           zone=None,
                           cluster_id=None,
                           retry=google.api_core.gapic_v1.method.DEFAULT,
                           timeout=google.api_core.gapic_v1.method.DEFAULT,
                           metadata=None):
        """
        Start master IP rotation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> # TODO: Initialize ``rotate_credentials``:
            >>> rotate_credentials = False
            >>>
            >>> response = client.start_i_p_rotation(name, rotate_credentials)

        Args:
            name (str): The name (project, location, cluster id) of the cluster to start IP
                rotation. Specified in the format 'projects/*/locations/*/clusters/*'.
            rotate_credentials (bool): Whether to rotate credentials during IP rotation.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'start_i_p_rotation' not in self._inner_api_calls:
            self._inner_api_calls[
                'start_i_p_rotation'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.start_i_p_rotation,
                    default_retry=self._method_configs['StartIPRotation'].
                    retry,
                    default_timeout=self._method_configs['StartIPRotation'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.StartIPRotationRequest(
            name=name,
            rotate_credentials=rotate_credentials,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['start_i_p_rotation'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def complete_i_p_rotation(self,
                              name,
                              project_id=None,
                              zone=None,
                              cluster_id=None,
                              retry=google.api_core.gapic_v1.method.DEFAULT,
                              timeout=google.api_core.gapic_v1.method.DEFAULT,
                              metadata=None):
        """
        Completes master IP rotation.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.complete_i_p_rotation(name)

        Args:
            name (str): The name (project, location, cluster id) of the cluster to complete IP
                rotation. Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'complete_i_p_rotation' not in self._inner_api_calls:
            self._inner_api_calls[
                'complete_i_p_rotation'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.complete_i_p_rotation,
                    default_retry=self._method_configs['CompleteIPRotation'].
                    retry,
                    default_timeout=self._method_configs['CompleteIPRotation'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.CompleteIPRotationRequest(
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['complete_i_p_rotation'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_node_pool_size(self,
                           node_count,
                           name,
                           project_id=None,
                           zone=None,
                           cluster_id=None,
                           node_pool_id=None,
                           retry=google.api_core.gapic_v1.method.DEFAULT,
                           timeout=google.api_core.gapic_v1.method.DEFAULT,
                           metadata=None):
        """
        Sets the size for a specific node pool.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``node_count``:
            >>> node_count = 0
            >>> name = client.node_pool_path('[PROJECT]', '[LOCATION]', '[CLUSTER]', '[NODE_POOL]')
            >>>
            >>> response = client.set_node_pool_size(node_count, name)

        Args:
            node_count (int): The desired node count for the pool.
            name (str): The name (project, location, cluster, node pool id) of the node pool to set
                size.
                Specified in the format 'projects/*/locations/*/clusters/*/nodePools/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster to update.
                This field has been deprecated and replaced by the name field.
            node_pool_id (str): Deprecated. The name of the node pool to update.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_node_pool_size' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_node_pool_size'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_node_pool_size,
                    default_retry=self._method_configs['SetNodePoolSize'].
                    retry,
                    default_timeout=self._method_configs['SetNodePoolSize'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetNodePoolSizeRequest(
            node_count=node_count,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
        )
        return self._inner_api_calls['set_node_pool_size'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_network_policy(self,
                           network_policy,
                           name,
                           project_id=None,
                           zone=None,
                           cluster_id=None,
                           retry=google.api_core.gapic_v1.method.DEFAULT,
                           timeout=google.api_core.gapic_v1.method.DEFAULT,
                           metadata=None):
        """
        Enables/Disables Network Policy for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``network_policy``:
            >>> network_policy = {}
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_network_policy(network_policy, name)

        Args:
            network_policy (Union[dict, ~google.cloud.container_v1.types.NetworkPolicy]): Configuration options for the NetworkPolicy feature.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.NetworkPolicy`
            name (str): The name (project, location, cluster id) of the cluster to set networking
                policy. Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): Deprecated. The Google Developers Console [project ID or project
                number](https://developers.google.com/console/help/new/#projectnumber).
                This field has been deprecated and replaced by the name field.
            zone (str): Deprecated. The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
                This field has been deprecated and replaced by the name field.
            cluster_id (str): Deprecated. The name of the cluster.
                This field has been deprecated and replaced by the name field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_network_policy' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_network_policy'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_network_policy,
                    default_retry=self._method_configs['SetNetworkPolicy'].
                    retry,
                    default_timeout=self._method_configs['SetNetworkPolicy'].
                    timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetNetworkPolicyRequest(
            network_policy=network_policy,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_network_policy'](
            request, retry=retry, timeout=timeout, metadata=metadata)

    def set_maintenance_policy(self,
                               maintenance_policy,
                               name,
                               project_id=None,
                               zone=None,
                               cluster_id=None,
                               retry=google.api_core.gapic_v1.method.DEFAULT,
                               timeout=google.api_core.gapic_v1.method.DEFAULT,
                               metadata=None):
        """
        Sets the maintenance policy for a cluster.

        Example:
            >>> from google.cloud import container_v1
            >>>
            >>> client = container_v1.ClusterManagerClient()
            >>>
            >>> # TODO: Initialize ``maintenance_policy``:
            >>> maintenance_policy = {}
            >>> name = client.cluster_path('[PROJECT]', '[LOCATION]', '[CLUSTER]')
            >>>
            >>> response = client.set_maintenance_policy(maintenance_policy, name)

        Args:
            maintenance_policy (Union[dict, ~google.cloud.container_v1.types.MaintenancePolicy]): The maintenance policy to be set for the cluster. An empty field
                clears the existing maintenance policy.
                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.container_v1.types.MaintenancePolicy`
            name (str): The name (project, location, cluster id) of the cluster to set maintenance
                policy.
                Specified in the format 'projects/*/locations/*/clusters/*'.
            project_id (str): The Google Developers Console [project ID or project
                number](https://support.google.com/cloud/answer/6158840).
            zone (str): The name of the Google Compute Engine
                `zone <https://cloud.google.com/compute/docs/zones#available>`_ in which the cluster
                resides.
            cluster_id (str): The name of the cluster to update.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will not
                be retried.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.container_v1.types.Operation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'set_maintenance_policy' not in self._inner_api_calls:
            self._inner_api_calls[
                'set_maintenance_policy'] = google.api_core.gapic_v1.method.wrap_method(
                    self.transport.set_maintenance_policy,
                    default_retry=self._method_configs['SetMaintenancePolicy'].
                    retry,
                    default_timeout=self.
                    _method_configs['SetMaintenancePolicy'].timeout,
                    client_info=self._client_info,
                )

        request = cluster_service_pb2.SetMaintenancePolicyRequest(
            maintenance_policy=maintenance_policy,
            name=name,
            project_id=project_id,
            zone=zone,
            cluster_id=cluster_id,
        )
        return self._inner_api_calls['set_maintenance_policy'](
            request, retry=retry, timeout=timeout, metadata=metadata)
