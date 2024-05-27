# kubevirt.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_migration_policy**](DefaultApi.md#create_migration_policy) | **POST** /apis/migrations.kubevirt.io/v1alpha1/migrationpolicies | 
[**create_namespaced_kube_virt**](DefaultApi.md#create_namespaced_kube_virt) | **POST** /apis/kubevirt.io/v1/namespaces/{namespace}/kubevirt | 
[**create_namespaced_virtual_machine**](DefaultApi.md#create_namespaced_virtual_machine) | **POST** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachines | 
[**create_namespaced_virtual_machine_export**](DefaultApi.md#create_namespaced_virtual_machine_export) | **POST** /apis/export.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachineexports | 
[**create_namespaced_virtual_machine_instance**](DefaultApi.md#create_namespaced_virtual_machine_instance) | **POST** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances | 
[**create_namespaced_virtual_machine_instance_migration**](DefaultApi.md#create_namespaced_virtual_machine_instance_migration) | **POST** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancemigrations | 
[**create_namespaced_virtual_machine_instance_preset**](DefaultApi.md#create_namespaced_virtual_machine_instance_preset) | **POST** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancepresets | 
[**create_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#create_namespaced_virtual_machine_instance_replica_set) | **POST** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancereplicasets | 
[**create_namespaced_virtual_machine_instancetype**](DefaultApi.md#create_namespaced_virtual_machine_instancetype) | **POST** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachineinstancetypes | 
[**create_namespaced_virtual_machine_pool**](DefaultApi.md#create_namespaced_virtual_machine_pool) | **POST** /apis/pool.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepools | 
[**create_namespaced_virtual_machine_preference**](DefaultApi.md#create_namespaced_virtual_machine_preference) | **POST** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinepreferences | 
[**create_namespaced_virtual_machine_restore**](DefaultApi.md#create_namespaced_virtual_machine_restore) | **POST** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinerestores | 
[**create_namespaced_virtual_machine_snapshot**](DefaultApi.md#create_namespaced_virtual_machine_snapshot) | **POST** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshots | 
[**create_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#create_namespaced_virtual_machine_snapshot_content) | **POST** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshotcontents | 
[**create_virtual_machine_clone**](DefaultApi.md#create_virtual_machine_clone) | **POST** /apis/clone.kubevirt.io/v1alpha1/virtualmachineclones | 
[**create_virtual_machine_cluster_instancetype**](DefaultApi.md#create_virtual_machine_cluster_instancetype) | **POST** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterinstancetypes | 
[**create_virtual_machine_cluster_preference**](DefaultApi.md#create_virtual_machine_cluster_preference) | **POST** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterpreferences | 
[**delete_collection_migration_policy**](DefaultApi.md#delete_collection_migration_policy) | **DELETE** /apis/migrations.kubevirt.io/v1alpha1/migrationpolicies | 
[**delete_collection_namespaced_kube_virt**](DefaultApi.md#delete_collection_namespaced_kube_virt) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/kubevirt | 
[**delete_collection_namespaced_virtual_machine**](DefaultApi.md#delete_collection_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachines | 
[**delete_collection_namespaced_virtual_machine_export**](DefaultApi.md#delete_collection_namespaced_virtual_machine_export) | **DELETE** /apis/export.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachineexports | 
[**delete_collection_namespaced_virtual_machine_instance**](DefaultApi.md#delete_collection_namespaced_virtual_machine_instance) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances | 
[**delete_collection_namespaced_virtual_machine_instance_migration**](DefaultApi.md#delete_collection_namespaced_virtual_machine_instance_migration) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancemigrations | 
[**delete_collection_namespaced_virtual_machine_instance_preset**](DefaultApi.md#delete_collection_namespaced_virtual_machine_instance_preset) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancepresets | 
[**delete_collection_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#delete_collection_namespaced_virtual_machine_instance_replica_set) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancereplicasets | 
[**delete_collection_namespaced_virtual_machine_instancetype**](DefaultApi.md#delete_collection_namespaced_virtual_machine_instancetype) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachineinstancetypes | 
[**delete_collection_namespaced_virtual_machine_pool**](DefaultApi.md#delete_collection_namespaced_virtual_machine_pool) | **DELETE** /apis/pool.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepools | 
[**delete_collection_namespaced_virtual_machine_preference**](DefaultApi.md#delete_collection_namespaced_virtual_machine_preference) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinepreferences | 
[**delete_collection_namespaced_virtual_machine_restore**](DefaultApi.md#delete_collection_namespaced_virtual_machine_restore) | **DELETE** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinerestores | 
[**delete_collection_namespaced_virtual_machine_snapshot**](DefaultApi.md#delete_collection_namespaced_virtual_machine_snapshot) | **DELETE** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshots | 
[**delete_collection_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#delete_collection_namespaced_virtual_machine_snapshot_content) | **DELETE** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshotcontents | 
[**delete_collection_virtual_machine_clone**](DefaultApi.md#delete_collection_virtual_machine_clone) | **DELETE** /apis/clone.kubevirt.io/v1alpha1/virtualmachineclones | 
[**delete_collection_virtual_machine_cluster_instancetype**](DefaultApi.md#delete_collection_virtual_machine_cluster_instancetype) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterinstancetypes | 
[**delete_collection_virtual_machine_cluster_preference**](DefaultApi.md#delete_collection_virtual_machine_cluster_preference) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterpreferences | 
[**delete_migration_policy**](DefaultApi.md#delete_migration_policy) | **DELETE** /apis/migrations.kubevirt.io/v1alpha1/migrationpolicies/{name} | 
[**delete_namespaced_kube_virt**](DefaultApi.md#delete_namespaced_kube_virt) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/kubevirt/{name} | 
[**delete_namespaced_virtual_machine**](DefaultApi.md#delete_namespaced_virtual_machine) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name} | 
[**delete_namespaced_virtual_machine_export**](DefaultApi.md#delete_namespaced_virtual_machine_export) | **DELETE** /apis/export.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachineexports/{name} | 
[**delete_namespaced_virtual_machine_instance**](DefaultApi.md#delete_namespaced_virtual_machine_instance) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name} | 
[**delete_namespaced_virtual_machine_instance_migration**](DefaultApi.md#delete_namespaced_virtual_machine_instance_migration) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | 
[**delete_namespaced_virtual_machine_instance_preset**](DefaultApi.md#delete_namespaced_virtual_machine_instance_preset) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancepresets/{name} | 
[**delete_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#delete_namespaced_virtual_machine_instance_replica_set) | **DELETE** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | 
[**delete_namespaced_virtual_machine_instancetype**](DefaultApi.md#delete_namespaced_virtual_machine_instancetype) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachineinstancetypes/{name} | 
[**delete_namespaced_virtual_machine_pool**](DefaultApi.md#delete_namespaced_virtual_machine_pool) | **DELETE** /apis/pool.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepools/{name} | 
[**delete_namespaced_virtual_machine_preference**](DefaultApi.md#delete_namespaced_virtual_machine_preference) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinepreferences/{name} | 
[**delete_namespaced_virtual_machine_restore**](DefaultApi.md#delete_namespaced_virtual_machine_restore) | **DELETE** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinerestores/{name} | 
[**delete_namespaced_virtual_machine_snapshot**](DefaultApi.md#delete_namespaced_virtual_machine_snapshot) | **DELETE** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshots/{name} | 
[**delete_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#delete_namespaced_virtual_machine_snapshot_content) | **DELETE** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshotcontents/{name} | 
[**delete_virtual_machine_clone**](DefaultApi.md#delete_virtual_machine_clone) | **DELETE** /apis/clone.kubevirt.io/v1alpha1/virtualmachineclones/{name} | 
[**delete_virtual_machine_cluster_instancetype**](DefaultApi.md#delete_virtual_machine_cluster_instancetype) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterinstancetypes/{name} | 
[**delete_virtual_machine_cluster_preference**](DefaultApi.md#delete_virtual_machine_cluster_preference) | **DELETE** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterpreferences/{name} | 
[**func13**](DefaultApi.md#func13) | **GET** /healthz | 
[**func6**](DefaultApi.md#func6) | **GET** /openapi/v2 | 
[**get_api_group_clone_kubevirt_io**](DefaultApi.md#get_api_group_clone_kubevirt_io) | **GET** /apis/clone.kubevirt.io/ | 
[**get_api_group_export_kubevirt_io**](DefaultApi.md#get_api_group_export_kubevirt_io) | **GET** /apis/export.kubevirt.io/ | 
[**get_api_group_instancetype_kubevirt_io**](DefaultApi.md#get_api_group_instancetype_kubevirt_io) | **GET** /apis/instancetype.kubevirt.io/ | 
[**get_api_group_kubevirt_io**](DefaultApi.md#get_api_group_kubevirt_io) | **GET** /apis/kubevirt.io/ | 
[**get_api_group_list**](DefaultApi.md#get_api_group_list) | **GET** /apis | 
[**get_api_group_migrations_kubevirt_io**](DefaultApi.md#get_api_group_migrations_kubevirt_io) | **GET** /apis/migrations.kubevirt.io/ | 
[**get_api_group_pool_kubevirt_io**](DefaultApi.md#get_api_group_pool_kubevirt_io) | **GET** /apis/pool.kubevirt.io/ | 
[**get_api_group_snapshot_kubevirt_io**](DefaultApi.md#get_api_group_snapshot_kubevirt_io) | **GET** /apis/snapshot.kubevirt.io/ | 
[**get_api_resources_clone_kubevirt_io_v1alpha1**](DefaultApi.md#get_api_resources_clone_kubevirt_io_v1alpha1) | **GET** /apis/clone.kubevirt.io/v1alpha1/ | 
[**get_api_resources_export_kubevirt_io_v1alpha1**](DefaultApi.md#get_api_resources_export_kubevirt_io_v1alpha1) | **GET** /apis/export.kubevirt.io/v1alpha1/ | 
[**get_api_resources_instancetype_kubevirt_io_v1beta1**](DefaultApi.md#get_api_resources_instancetype_kubevirt_io_v1beta1) | **GET** /apis/instancetype.kubevirt.io/v1beta1/ | 
[**get_api_resources_kubevirt_io_v1**](DefaultApi.md#get_api_resources_kubevirt_io_v1) | **GET** /apis/kubevirt.io/v1/ | 
[**get_api_resources_migrations_kubevirt_io_v1alpha1**](DefaultApi.md#get_api_resources_migrations_kubevirt_io_v1alpha1) | **GET** /apis/migrations.kubevirt.io/v1alpha1/ | 
[**get_api_resources_pool_kubevirt_io_v1alpha1**](DefaultApi.md#get_api_resources_pool_kubevirt_io_v1alpha1) | **GET** /apis/pool.kubevirt.io/v1alpha1/ | 
[**get_api_resources_snapshot_kubevirt_io_v1beta1**](DefaultApi.md#get_api_resources_snapshot_kubevirt_io_v1beta1) | **GET** /apis/snapshot.kubevirt.io/v1beta1/ | 
[**get_root_paths**](DefaultApi.md#get_root_paths) | **GET** / | 
[**handle_dump_profiler**](DefaultApi.md#handle_dump_profiler) | **GET** /dump-profiler | 
[**handle_start_profiler**](DefaultApi.md#handle_start_profiler) | **GET** /start-profiler | 
[**handle_stop_profiler**](DefaultApi.md#handle_stop_profiler) | **GET** /stop-profiler | 
[**list_kube_virt_for_all_namespaces**](DefaultApi.md#list_kube_virt_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/kubevirt | 
[**list_migration_policy**](DefaultApi.md#list_migration_policy) | **GET** /apis/migrations.kubevirt.io/v1alpha1/migrationpolicies | 
[**list_namespaced_kube_virt**](DefaultApi.md#list_namespaced_kube_virt) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/kubevirt | 
[**list_namespaced_virtual_machine**](DefaultApi.md#list_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachines | 
[**list_namespaced_virtual_machine_export**](DefaultApi.md#list_namespaced_virtual_machine_export) | **GET** /apis/export.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachineexports | 
[**list_namespaced_virtual_machine_instance**](DefaultApi.md#list_namespaced_virtual_machine_instance) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances | 
[**list_namespaced_virtual_machine_instance_migration**](DefaultApi.md#list_namespaced_virtual_machine_instance_migration) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancemigrations | 
[**list_namespaced_virtual_machine_instance_preset**](DefaultApi.md#list_namespaced_virtual_machine_instance_preset) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancepresets | 
[**list_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#list_namespaced_virtual_machine_instance_replica_set) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancereplicasets | 
[**list_namespaced_virtual_machine_instancetype**](DefaultApi.md#list_namespaced_virtual_machine_instancetype) | **GET** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachineinstancetypes | 
[**list_namespaced_virtual_machine_pool**](DefaultApi.md#list_namespaced_virtual_machine_pool) | **GET** /apis/pool.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepools | 
[**list_namespaced_virtual_machine_preference**](DefaultApi.md#list_namespaced_virtual_machine_preference) | **GET** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinepreferences | 
[**list_namespaced_virtual_machine_restore**](DefaultApi.md#list_namespaced_virtual_machine_restore) | **GET** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinerestores | 
[**list_namespaced_virtual_machine_snapshot**](DefaultApi.md#list_namespaced_virtual_machine_snapshot) | **GET** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshots | 
[**list_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#list_namespaced_virtual_machine_snapshot_content) | **GET** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshotcontents | 
[**list_virtual_machine_clone**](DefaultApi.md#list_virtual_machine_clone) | **GET** /apis/clone.kubevirt.io/v1alpha1/virtualmachineclones | 
[**list_virtual_machine_cluster_instancetype**](DefaultApi.md#list_virtual_machine_cluster_instancetype) | **GET** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterinstancetypes | 
[**list_virtual_machine_cluster_preference**](DefaultApi.md#list_virtual_machine_cluster_preference) | **GET** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterpreferences | 
[**list_virtual_machine_export_for_all_namespaces**](DefaultApi.md#list_virtual_machine_export_for_all_namespaces) | **GET** /apis/export.kubevirt.io/v1alpha1/virtualmachineexports | 
[**list_virtual_machine_for_all_namespaces**](DefaultApi.md#list_virtual_machine_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/virtualmachines | 
[**list_virtual_machine_instance_for_all_namespaces**](DefaultApi.md#list_virtual_machine_instance_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/virtualmachineinstances | 
[**list_virtual_machine_instance_migration_for_all_namespaces**](DefaultApi.md#list_virtual_machine_instance_migration_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/virtualmachineinstancemigrations | 
[**list_virtual_machine_instance_preset_for_all_namespaces**](DefaultApi.md#list_virtual_machine_instance_preset_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/virtualmachineinstancepresets | 
[**list_virtual_machine_instance_replica_set_for_all_namespaces**](DefaultApi.md#list_virtual_machine_instance_replica_set_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/virtualmachineinstancereplicasets | 
[**list_virtual_machine_instancetype_for_all_namespaces**](DefaultApi.md#list_virtual_machine_instancetype_for_all_namespaces) | **GET** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineinstancetypes | 
[**list_virtual_machine_pool_for_all_namespaces**](DefaultApi.md#list_virtual_machine_pool_for_all_namespaces) | **GET** /apis/pool.kubevirt.io/v1alpha1/virtualmachinepools | 
[**list_virtual_machine_preference_for_all_namespaces**](DefaultApi.md#list_virtual_machine_preference_for_all_namespaces) | **GET** /apis/instancetype.kubevirt.io/v1beta1/virtualmachinepreferences | 
[**list_virtual_machine_restore_for_all_namespaces**](DefaultApi.md#list_virtual_machine_restore_for_all_namespaces) | **GET** /apis/snapshot.kubevirt.io/v1beta1/virtualmachinerestores | 
[**list_virtual_machine_snapshot_content_for_all_namespaces**](DefaultApi.md#list_virtual_machine_snapshot_content_for_all_namespaces) | **GET** /apis/snapshot.kubevirt.io/v1beta1/virtualmachinesnapshotcontents | 
[**list_virtual_machine_snapshot_for_all_namespaces**](DefaultApi.md#list_virtual_machine_snapshot_for_all_namespaces) | **GET** /apis/snapshot.kubevirt.io/v1beta1/virtualmachinesnapshots | 
[**patch_migration_policy**](DefaultApi.md#patch_migration_policy) | **PATCH** /apis/migrations.kubevirt.io/v1alpha1/migrationpolicies/{name} | 
[**patch_namespaced_kube_virt**](DefaultApi.md#patch_namespaced_kube_virt) | **PATCH** /apis/kubevirt.io/v1/namespaces/{namespace}/kubevirt/{name} | 
[**patch_namespaced_virtual_machine**](DefaultApi.md#patch_namespaced_virtual_machine) | **PATCH** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name} | 
[**patch_namespaced_virtual_machine_export**](DefaultApi.md#patch_namespaced_virtual_machine_export) | **PATCH** /apis/export.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachineexports/{name} | 
[**patch_namespaced_virtual_machine_instance**](DefaultApi.md#patch_namespaced_virtual_machine_instance) | **PATCH** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name} | 
[**patch_namespaced_virtual_machine_instance_migration**](DefaultApi.md#patch_namespaced_virtual_machine_instance_migration) | **PATCH** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | 
[**patch_namespaced_virtual_machine_instance_preset**](DefaultApi.md#patch_namespaced_virtual_machine_instance_preset) | **PATCH** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancepresets/{name} | 
[**patch_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#patch_namespaced_virtual_machine_instance_replica_set) | **PATCH** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | 
[**patch_namespaced_virtual_machine_instancetype**](DefaultApi.md#patch_namespaced_virtual_machine_instancetype) | **PATCH** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachineinstancetypes/{name} | 
[**patch_namespaced_virtual_machine_pool**](DefaultApi.md#patch_namespaced_virtual_machine_pool) | **PATCH** /apis/pool.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepools/{name} | 
[**patch_namespaced_virtual_machine_preference**](DefaultApi.md#patch_namespaced_virtual_machine_preference) | **PATCH** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinepreferences/{name} | 
[**patch_namespaced_virtual_machine_restore**](DefaultApi.md#patch_namespaced_virtual_machine_restore) | **PATCH** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinerestores/{name} | 
[**patch_namespaced_virtual_machine_snapshot**](DefaultApi.md#patch_namespaced_virtual_machine_snapshot) | **PATCH** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshots/{name} | 
[**patch_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#patch_namespaced_virtual_machine_snapshot_content) | **PATCH** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshotcontents/{name} | 
[**patch_virtual_machine_clone**](DefaultApi.md#patch_virtual_machine_clone) | **PATCH** /apis/clone.kubevirt.io/v1alpha1/virtualmachineclones/{name} | 
[**patch_virtual_machine_cluster_instancetype**](DefaultApi.md#patch_virtual_machine_cluster_instancetype) | **PATCH** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterinstancetypes/{name} | 
[**patch_virtual_machine_cluster_preference**](DefaultApi.md#patch_virtual_machine_cluster_preference) | **PATCH** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterpreferences/{name} | 
[**read_migration_policy**](DefaultApi.md#read_migration_policy) | **GET** /apis/migrations.kubevirt.io/v1alpha1/migrationpolicies/{name} | 
[**read_namespaced_kube_virt**](DefaultApi.md#read_namespaced_kube_virt) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/kubevirt/{name} | 
[**read_namespaced_virtual_machine**](DefaultApi.md#read_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name} | 
[**read_namespaced_virtual_machine_export**](DefaultApi.md#read_namespaced_virtual_machine_export) | **GET** /apis/export.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachineexports/{name} | 
[**read_namespaced_virtual_machine_instance**](DefaultApi.md#read_namespaced_virtual_machine_instance) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name} | 
[**read_namespaced_virtual_machine_instance_migration**](DefaultApi.md#read_namespaced_virtual_machine_instance_migration) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | 
[**read_namespaced_virtual_machine_instance_preset**](DefaultApi.md#read_namespaced_virtual_machine_instance_preset) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancepresets/{name} | 
[**read_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#read_namespaced_virtual_machine_instance_replica_set) | **GET** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | 
[**read_namespaced_virtual_machine_instancetype**](DefaultApi.md#read_namespaced_virtual_machine_instancetype) | **GET** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachineinstancetypes/{name} | 
[**read_namespaced_virtual_machine_pool**](DefaultApi.md#read_namespaced_virtual_machine_pool) | **GET** /apis/pool.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepools/{name} | 
[**read_namespaced_virtual_machine_preference**](DefaultApi.md#read_namespaced_virtual_machine_preference) | **GET** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinepreferences/{name} | 
[**read_namespaced_virtual_machine_restore**](DefaultApi.md#read_namespaced_virtual_machine_restore) | **GET** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinerestores/{name} | 
[**read_namespaced_virtual_machine_snapshot**](DefaultApi.md#read_namespaced_virtual_machine_snapshot) | **GET** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshots/{name} | 
[**read_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#read_namespaced_virtual_machine_snapshot_content) | **GET** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshotcontents/{name} | 
[**read_virtual_machine_clone**](DefaultApi.md#read_virtual_machine_clone) | **GET** /apis/clone.kubevirt.io/v1alpha1/virtualmachineclones/{name} | 
[**read_virtual_machine_cluster_instancetype**](DefaultApi.md#read_virtual_machine_cluster_instancetype) | **GET** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterinstancetypes/{name} | 
[**read_virtual_machine_cluster_preference**](DefaultApi.md#read_virtual_machine_cluster_preference) | **GET** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterpreferences/{name} | 
[**replace_migration_policy**](DefaultApi.md#replace_migration_policy) | **PUT** /apis/migrations.kubevirt.io/v1alpha1/migrationpolicies/{name} | 
[**replace_namespaced_kube_virt**](DefaultApi.md#replace_namespaced_kube_virt) | **PUT** /apis/kubevirt.io/v1/namespaces/{namespace}/kubevirt/{name} | 
[**replace_namespaced_virtual_machine**](DefaultApi.md#replace_namespaced_virtual_machine) | **PUT** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name} | 
[**replace_namespaced_virtual_machine_export**](DefaultApi.md#replace_namespaced_virtual_machine_export) | **PUT** /apis/export.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachineexports/{name} | 
[**replace_namespaced_virtual_machine_instance**](DefaultApi.md#replace_namespaced_virtual_machine_instance) | **PUT** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name} | 
[**replace_namespaced_virtual_machine_instance_migration**](DefaultApi.md#replace_namespaced_virtual_machine_instance_migration) | **PUT** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancemigrations/{name} | 
[**replace_namespaced_virtual_machine_instance_preset**](DefaultApi.md#replace_namespaced_virtual_machine_instance_preset) | **PUT** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancepresets/{name} | 
[**replace_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#replace_namespaced_virtual_machine_instance_replica_set) | **PUT** /apis/kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstancereplicasets/{name} | 
[**replace_namespaced_virtual_machine_instancetype**](DefaultApi.md#replace_namespaced_virtual_machine_instancetype) | **PUT** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachineinstancetypes/{name} | 
[**replace_namespaced_virtual_machine_pool**](DefaultApi.md#replace_namespaced_virtual_machine_pool) | **PUT** /apis/pool.kubevirt.io/v1alpha1/namespaces/{namespace}/virtualmachinepools/{name} | 
[**replace_namespaced_virtual_machine_preference**](DefaultApi.md#replace_namespaced_virtual_machine_preference) | **PUT** /apis/instancetype.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinepreferences/{name} | 
[**replace_namespaced_virtual_machine_restore**](DefaultApi.md#replace_namespaced_virtual_machine_restore) | **PUT** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinerestores/{name} | 
[**replace_namespaced_virtual_machine_snapshot**](DefaultApi.md#replace_namespaced_virtual_machine_snapshot) | **PUT** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshots/{name} | 
[**replace_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#replace_namespaced_virtual_machine_snapshot_content) | **PUT** /apis/snapshot.kubevirt.io/v1beta1/namespaces/{namespace}/virtualmachinesnapshotcontents/{name} | 
[**replace_virtual_machine_clone**](DefaultApi.md#replace_virtual_machine_clone) | **PUT** /apis/clone.kubevirt.io/v1alpha1/virtualmachineclones/{name} | 
[**replace_virtual_machine_cluster_instancetype**](DefaultApi.md#replace_virtual_machine_cluster_instancetype) | **PUT** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterinstancetypes/{name} | 
[**replace_virtual_machine_cluster_preference**](DefaultApi.md#replace_virtual_machine_cluster_preference) | **PUT** /apis/instancetype.kubevirt.io/v1beta1/virtualmachineclusterpreferences/{name} | 
[**v1_check_health**](DefaultApi.md#v1_check_health) | **GET** /apis/subresources.kubevirt.io/v1/healthz | 
[**v1_console**](DefaultApi.md#v1_console) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/console | 
[**v1_expand_spec**](DefaultApi.md#v1_expand_spec) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/expand-vm-spec | 
[**v1_filesystemlist**](DefaultApi.md#v1_filesystemlist) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/filesystemlist | 
[**v1_freeze**](DefaultApi.md#v1_freeze) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/freeze | 
[**v1_get_sub_api_group**](DefaultApi.md#v1_get_sub_api_group) | **GET** /apis/subresources.kubevirt.io | 
[**v1_guestfs**](DefaultApi.md#v1_guestfs) | **GET** /apis/subresources.kubevirt.io/v1/guestfs | 
[**v1_guestosinfo**](DefaultApi.md#v1_guestosinfo) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/guestosinfo | 
[**v1_memory_dump**](DefaultApi.md#v1_memory_dump) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/memorydump | 
[**v1_migrate**](DefaultApi.md#v1_migrate) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/migrate | 
[**v1_pause**](DefaultApi.md#v1_pause) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/pause | 
[**v1_remove_memory_dump**](DefaultApi.md#v1_remove_memory_dump) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/removememorydump | 
[**v1_restart**](DefaultApi.md#v1_restart) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/restart | 
[**v1_sev_fetch_cert_chain**](DefaultApi.md#v1_sev_fetch_cert_chain) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/sev/fetchcertchain | 
[**v1_sev_inject_launch_secret**](DefaultApi.md#v1_sev_inject_launch_secret) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/sev/injectlaunchsecret | 
[**v1_sev_query_launch_measurement**](DefaultApi.md#v1_sev_query_launch_measurement) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/sev/querylaunchmeasurement | 
[**v1_sev_setup_session**](DefaultApi.md#v1_sev_setup_session) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/sev/setupsession | 
[**v1_soft_reboot**](DefaultApi.md#v1_soft_reboot) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/softreboot | 
[**v1_start**](DefaultApi.md#v1_start) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/start | 
[**v1_stop**](DefaultApi.md#v1_stop) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/stop | 
[**v1_unfreeze**](DefaultApi.md#v1_unfreeze) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/unfreeze | 
[**v1_unpause**](DefaultApi.md#v1_unpause) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/unpause | 
[**v1_userlist**](DefaultApi.md#v1_userlist) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/userlist | 
[**v1_version**](DefaultApi.md#v1_version) | **GET** /apis/subresources.kubevirt.io/v1/version | 
[**v1_vnc**](DefaultApi.md#v1_vnc) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/vnc | 
[**v1_vnc_screenshot**](DefaultApi.md#v1_vnc_screenshot) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/vnc/screenshot | 
[**v1_vsock**](DefaultApi.md#v1_vsock) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/vsock | 
[**v1alpha3_check_health**](DefaultApi.md#v1alpha3_check_health) | **GET** /apis/subresources.kubevirt.io/v1alpha3/healthz | 
[**v1alpha3_console**](DefaultApi.md#v1alpha3_console) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/console | 
[**v1alpha3_expand_spec**](DefaultApi.md#v1alpha3_expand_spec) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/expand-vm-spec | 
[**v1alpha3_filesystemlist**](DefaultApi.md#v1alpha3_filesystemlist) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/filesystemlist | 
[**v1alpha3_freeze**](DefaultApi.md#v1alpha3_freeze) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/freeze | 
[**v1alpha3_guestfs**](DefaultApi.md#v1alpha3_guestfs) | **GET** /apis/subresources.kubevirt.io/v1alpha3/guestfs | 
[**v1alpha3_guestosinfo**](DefaultApi.md#v1alpha3_guestosinfo) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/guestosinfo | 
[**v1alpha3_memory_dump**](DefaultApi.md#v1alpha3_memory_dump) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/memorydump | 
[**v1alpha3_migrate**](DefaultApi.md#v1alpha3_migrate) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/migrate | 
[**v1alpha3_pause**](DefaultApi.md#v1alpha3_pause) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/pause | 
[**v1alpha3_remove_memory_dump**](DefaultApi.md#v1alpha3_remove_memory_dump) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/removememorydump | 
[**v1alpha3_restart**](DefaultApi.md#v1alpha3_restart) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/restart | 
[**v1alpha3_sev_fetch_cert_chain**](DefaultApi.md#v1alpha3_sev_fetch_cert_chain) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/sev/fetchcertchain | 
[**v1alpha3_sev_inject_launch_secret**](DefaultApi.md#v1alpha3_sev_inject_launch_secret) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/sev/injectlaunchsecret | 
[**v1alpha3_sev_query_launch_measurement**](DefaultApi.md#v1alpha3_sev_query_launch_measurement) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/sev/querylaunchmeasurement | 
[**v1alpha3_sev_setup_session**](DefaultApi.md#v1alpha3_sev_setup_session) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/sev/setupsession | 
[**v1alpha3_soft_reboot**](DefaultApi.md#v1alpha3_soft_reboot) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/softreboot | 
[**v1alpha3_start**](DefaultApi.md#v1alpha3_start) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/start | 
[**v1alpha3_stop**](DefaultApi.md#v1alpha3_stop) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/stop | 
[**v1alpha3_unfreeze**](DefaultApi.md#v1alpha3_unfreeze) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/unfreeze | 
[**v1alpha3_unpause**](DefaultApi.md#v1alpha3_unpause) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/unpause | 
[**v1alpha3_userlist**](DefaultApi.md#v1alpha3_userlist) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/userlist | 
[**v1alpha3_version**](DefaultApi.md#v1alpha3_version) | **GET** /apis/subresources.kubevirt.io/v1alpha3/version | 
[**v1alpha3_vnc**](DefaultApi.md#v1alpha3_vnc) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/vnc | 
[**v1alpha3_vnc_screenshot**](DefaultApi.md#v1alpha3_vnc_screenshot) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/vnc/screenshot | 
[**v1alpha3_vsock**](DefaultApi.md#v1alpha3_vsock) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/vsock | 
[**v1alpha3dump_cluster_profiler**](DefaultApi.md#v1alpha3dump_cluster_profiler) | **GET** /apis/subresources.kubevirt.io/v1alpha3/dump-cluster-profiler | 
[**v1alpha3get_api_sub_resources**](DefaultApi.md#v1alpha3get_api_sub_resources) | **GET** /apis/subresources.kubevirt.io/v1alpha3/ | 
[**v1alpha3start_cluster_profiler**](DefaultApi.md#v1alpha3start_cluster_profiler) | **GET** /apis/subresources.kubevirt.io/v1alpha3/start-cluster-profiler | 
[**v1alpha3stop_cluster_profiler**](DefaultApi.md#v1alpha3stop_cluster_profiler) | **GET** /apis/subresources.kubevirt.io/v1alpha3/stop-cluster-profiler | 
[**v1alpha3usbredir**](DefaultApi.md#v1alpha3usbredir) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/usbredir | 
[**v1alpha3vm_addvolume**](DefaultApi.md#v1alpha3vm_addvolume) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/addvolume | 
[**v1alpha3vm_expand_spec**](DefaultApi.md#v1alpha3vm_expand_spec) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/expand-spec | 
[**v1alpha3vm_port_forward**](DefaultApi.md#v1alpha3vm_port_forward) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/portforward/{port} | 
[**v1alpha3vm_port_forward_with_protocol**](DefaultApi.md#v1alpha3vm_port_forward_with_protocol) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/portforward/{port}/{protocol} | 
[**v1alpha3vm_removevolume**](DefaultApi.md#v1alpha3vm_removevolume) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachines/{name}/removevolume | 
[**v1alpha3vmi_addvolume**](DefaultApi.md#v1alpha3vmi_addvolume) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/addvolume | 
[**v1alpha3vmi_port_forward**](DefaultApi.md#v1alpha3vmi_port_forward) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/portforward/{port} | 
[**v1alpha3vmi_port_forward_with_protocol**](DefaultApi.md#v1alpha3vmi_port_forward_with_protocol) | **GET** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/portforward/{port}/{protocol} | 
[**v1alpha3vmi_removevolume**](DefaultApi.md#v1alpha3vmi_removevolume) | **PUT** /apis/subresources.kubevirt.io/v1alpha3/namespaces/{namespace}/virtualmachineinstances/{name}/removevolume | 
[**v1dump_cluster_profiler**](DefaultApi.md#v1dump_cluster_profiler) | **GET** /apis/subresources.kubevirt.io/v1/dump-cluster-profiler | 
[**v1get_api_sub_resources**](DefaultApi.md#v1get_api_sub_resources) | **GET** /apis/subresources.kubevirt.io/v1/ | 
[**v1start_cluster_profiler**](DefaultApi.md#v1start_cluster_profiler) | **GET** /apis/subresources.kubevirt.io/v1/start-cluster-profiler | 
[**v1stop_cluster_profiler**](DefaultApi.md#v1stop_cluster_profiler) | **GET** /apis/subresources.kubevirt.io/v1/stop-cluster-profiler | 
[**v1usbredir**](DefaultApi.md#v1usbredir) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/usbredir | 
[**v1vm_addvolume**](DefaultApi.md#v1vm_addvolume) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/addvolume | 
[**v1vm_expand_spec**](DefaultApi.md#v1vm_expand_spec) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/expand-spec | 
[**v1vm_port_forward**](DefaultApi.md#v1vm_port_forward) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/portforward/{port} | 
[**v1vm_port_forward_with_protocol**](DefaultApi.md#v1vm_port_forward_with_protocol) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/portforward/{port}/{protocol} | 
[**v1vm_removevolume**](DefaultApi.md#v1vm_removevolume) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachines/{name}/removevolume | 
[**v1vmi_addvolume**](DefaultApi.md#v1vmi_addvolume) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/addvolume | 
[**v1vmi_port_forward**](DefaultApi.md#v1vmi_port_forward) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/portforward/{port} | 
[**v1vmi_port_forward_with_protocol**](DefaultApi.md#v1vmi_port_forward_with_protocol) | **GET** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/portforward/{port}/{protocol} | 
[**v1vmi_removevolume**](DefaultApi.md#v1vmi_removevolume) | **PUT** /apis/subresources.kubevirt.io/v1/namespaces/{namespace}/virtualmachineinstances/{name}/removevolume | 
[**watch_kube_virt_list_for_all_namespaces**](DefaultApi.md#watch_kube_virt_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/watch/kubevirt | 
[**watch_migration_policy_list_for_all_namespaces**](DefaultApi.md#watch_migration_policy_list_for_all_namespaces) | **GET** /apis/migrations.kubevirt.io/v1alpha1/watch/migrationpolicies | 
[**watch_namespaced_kube_virt**](DefaultApi.md#watch_namespaced_kube_virt) | **GET** /apis/kubevirt.io/v1/watch/namespaces/{namespace}/kubevirt | 
[**watch_namespaced_virtual_machine**](DefaultApi.md#watch_namespaced_virtual_machine) | **GET** /apis/kubevirt.io/v1/watch/namespaces/{namespace}/virtualmachines | 
[**watch_namespaced_virtual_machine_export**](DefaultApi.md#watch_namespaced_virtual_machine_export) | **GET** /apis/export.kubevirt.io/v1alpha1/watch/namespaces/{namespace}/virtualmachineexports | 
[**watch_namespaced_virtual_machine_instance**](DefaultApi.md#watch_namespaced_virtual_machine_instance) | **GET** /apis/kubevirt.io/v1/watch/namespaces/{namespace}/virtualmachineinstances | 
[**watch_namespaced_virtual_machine_instance_migration**](DefaultApi.md#watch_namespaced_virtual_machine_instance_migration) | **GET** /apis/kubevirt.io/v1/watch/namespaces/{namespace}/virtualmachineinstancemigrations | 
[**watch_namespaced_virtual_machine_instance_preset**](DefaultApi.md#watch_namespaced_virtual_machine_instance_preset) | **GET** /apis/kubevirt.io/v1/watch/namespaces/{namespace}/virtualmachineinstancepresets | 
[**watch_namespaced_virtual_machine_instance_replica_set**](DefaultApi.md#watch_namespaced_virtual_machine_instance_replica_set) | **GET** /apis/kubevirt.io/v1/watch/namespaces/{namespace}/virtualmachineinstancereplicasets | 
[**watch_namespaced_virtual_machine_instancetype**](DefaultApi.md#watch_namespaced_virtual_machine_instancetype) | **GET** /apis/instancetype.kubevirt.io/v1beta1/watch/namespaces/{namespace}/virtualmachineinstancetypes | 
[**watch_namespaced_virtual_machine_pool**](DefaultApi.md#watch_namespaced_virtual_machine_pool) | **GET** /apis/pool.kubevirt.io/v1alpha1/watch/namespaces/{namespace}/virtualmachinepools | 
[**watch_namespaced_virtual_machine_preference**](DefaultApi.md#watch_namespaced_virtual_machine_preference) | **GET** /apis/instancetype.kubevirt.io/v1beta1/watch/namespaces/{namespace}/virtualmachinepreferences | 
[**watch_namespaced_virtual_machine_restore**](DefaultApi.md#watch_namespaced_virtual_machine_restore) | **GET** /apis/snapshot.kubevirt.io/v1beta1/watch/namespaces/{namespace}/virtualmachinerestores | 
[**watch_namespaced_virtual_machine_snapshot**](DefaultApi.md#watch_namespaced_virtual_machine_snapshot) | **GET** /apis/snapshot.kubevirt.io/v1beta1/watch/namespaces/{namespace}/virtualmachinesnapshots | 
[**watch_namespaced_virtual_machine_snapshot_content**](DefaultApi.md#watch_namespaced_virtual_machine_snapshot_content) | **GET** /apis/snapshot.kubevirt.io/v1beta1/watch/namespaces/{namespace}/virtualmachinesnapshotcontents | 
[**watch_virtual_machine_clone_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_clone_list_for_all_namespaces) | **GET** /apis/clone.kubevirt.io/v1alpha1/watch/virtualmachineclones | 
[**watch_virtual_machine_cluster_instancetype_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_cluster_instancetype_list_for_all_namespaces) | **GET** /apis/instancetype.kubevirt.io/v1beta1/watch/virtualmachineclusterinstancetypes | 
[**watch_virtual_machine_cluster_preference_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_cluster_preference_list_for_all_namespaces) | **GET** /apis/instancetype.kubevirt.io/v1beta1/watch/virtualmachineclusterpreferences | 
[**watch_virtual_machine_export_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_export_list_for_all_namespaces) | **GET** /apis/export.kubevirt.io/v1alpha1/watch/virtualmachineexports | 
[**watch_virtual_machine_instance_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_instance_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/watch/virtualmachineinstances | 
[**watch_virtual_machine_instance_migration_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_instance_migration_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/watch/virtualmachineinstancemigrations | 
[**watch_virtual_machine_instance_preset_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_instance_preset_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/watch/virtualmachineinstancepresets | 
[**watch_virtual_machine_instance_replica_set_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_instance_replica_set_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/watch/virtualmachineinstancereplicasets | 
[**watch_virtual_machine_instancetype_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_instancetype_list_for_all_namespaces) | **GET** /apis/instancetype.kubevirt.io/v1beta1/watch/virtualmachineinstancetypes | 
[**watch_virtual_machine_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_list_for_all_namespaces) | **GET** /apis/kubevirt.io/v1/watch/virtualmachines | 
[**watch_virtual_machine_pool_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_pool_list_for_all_namespaces) | **GET** /apis/pool.kubevirt.io/v1alpha1/watch/virtualmachinepools | 
[**watch_virtual_machine_preference_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_preference_list_for_all_namespaces) | **GET** /apis/instancetype.kubevirt.io/v1beta1/watch/virtualmachinepreferences | 
[**watch_virtual_machine_restore_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_restore_list_for_all_namespaces) | **GET** /apis/snapshot.kubevirt.io/v1beta1/watch/virtualmachinerestores | 
[**watch_virtual_machine_snapshot_content_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_snapshot_content_list_for_all_namespaces) | **GET** /apis/snapshot.kubevirt.io/v1beta1/watch/virtualmachinesnapshotcontents | 
[**watch_virtual_machine_snapshot_list_for_all_namespaces**](DefaultApi.md#watch_virtual_machine_snapshot_list_for_all_namespaces) | **GET** /apis/snapshot.kubevirt.io/v1beta1/watch/virtualmachinesnapshots | 


# **create_migration_policy**
> V1alpha1MigrationPolicy create_migration_policy(body)



Create a MigrationPolicy object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1alpha1MigrationPolicy() # V1alpha1MigrationPolicy | 

try: 
    api_response = api_instance.create_migration_policy(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_migration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1MigrationPolicy**](V1alpha1MigrationPolicy.md)|  | 

### Return type

[**V1alpha1MigrationPolicy**](V1alpha1MigrationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_kube_virt**
> V1KubeVirt create_namespaced_kube_virt(body, namespace)



Create a KubeVirt object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1KubeVirt() # V1KubeVirt | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_kube_virt(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1KubeVirt**](V1KubeVirt.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1KubeVirt**](V1KubeVirt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine**
> V1VirtualMachine create_namespaced_virtual_machine(body, namespace)



Create a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachine() # V1VirtualMachine | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachine**](V1VirtualMachine.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_export**
> V1alpha1VirtualMachineExport create_namespaced_virtual_machine_export(body, namespace)



Create a VirtualMachineExport object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1alpha1VirtualMachineExport() # V1alpha1VirtualMachineExport | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_export(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1VirtualMachineExport**](V1alpha1VirtualMachineExport.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1alpha1VirtualMachineExport**](V1alpha1VirtualMachineExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_instance**
> V1VirtualMachineInstance create_namespaced_virtual_machine_instance(body, namespace)



Create a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachineInstance() # V1VirtualMachineInstance | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_instance(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineInstance**](V1VirtualMachineInstance.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstance**](V1VirtualMachineInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_instance_migration**
> V1VirtualMachineInstanceMigration create_namespaced_virtual_machine_instance_migration(body, namespace)



Create a VirtualMachineInstanceMigration object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachineInstanceMigration() # V1VirtualMachineInstanceMigration | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_instance_migration(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineInstanceMigration**](V1VirtualMachineInstanceMigration.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceMigration**](V1VirtualMachineInstanceMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_instance_preset**
> V1VirtualMachineInstancePreset create_namespaced_virtual_machine_instance_preset(body, namespace)



Create a VirtualMachineInstancePreset object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachineInstancePreset() # V1VirtualMachineInstancePreset | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_instance_preset(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineInstancePreset**](V1VirtualMachineInstancePreset.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstancePreset**](V1VirtualMachineInstancePreset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_instance_replica_set**
> V1VirtualMachineInstanceReplicaSet create_namespaced_virtual_machine_instance_replica_set(body, namespace)



Create a VirtualMachineInstanceReplicaSet object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1VirtualMachineInstanceReplicaSet() # V1VirtualMachineInstanceReplicaSet | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_instance_replica_set(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VirtualMachineInstanceReplicaSet**](V1VirtualMachineInstanceReplicaSet.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceReplicaSet**](V1VirtualMachineInstanceReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_instancetype**
> V1beta1VirtualMachineInstancetype create_namespaced_virtual_machine_instancetype(body, namespace)



Create a VirtualMachineInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1beta1VirtualMachineInstancetype() # V1beta1VirtualMachineInstancetype | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_instancetype(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1VirtualMachineInstancetype**](V1beta1VirtualMachineInstancetype.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1beta1VirtualMachineInstancetype**](V1beta1VirtualMachineInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_pool**
> V1alpha1VirtualMachinePool create_namespaced_virtual_machine_pool(body, namespace)



Create a VirtualMachinePool object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1alpha1VirtualMachinePool() # V1alpha1VirtualMachinePool | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_pool(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1VirtualMachinePool**](V1alpha1VirtualMachinePool.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1alpha1VirtualMachinePool**](V1alpha1VirtualMachinePool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_preference**
> V1beta1VirtualMachinePreference create_namespaced_virtual_machine_preference(body, namespace)



Create a VirtualMachinePreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1beta1VirtualMachinePreference() # V1beta1VirtualMachinePreference | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_preference(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1VirtualMachinePreference**](V1beta1VirtualMachinePreference.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1beta1VirtualMachinePreference**](V1beta1VirtualMachinePreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_restore**
> V1beta1VirtualMachineRestore create_namespaced_virtual_machine_restore(body, namespace)



Create a VirtualMachineRestore object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1beta1VirtualMachineRestore() # V1beta1VirtualMachineRestore | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_restore(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1VirtualMachineRestore**](V1beta1VirtualMachineRestore.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1beta1VirtualMachineRestore**](V1beta1VirtualMachineRestore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_snapshot**
> V1beta1VirtualMachineSnapshot create_namespaced_virtual_machine_snapshot(body, namespace)



Create a VirtualMachineSnapshot object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1beta1VirtualMachineSnapshot() # V1beta1VirtualMachineSnapshot | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_snapshot(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1VirtualMachineSnapshot**](V1beta1VirtualMachineSnapshot.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1beta1VirtualMachineSnapshot**](V1beta1VirtualMachineSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_virtual_machine_snapshot_content**
> V1beta1VirtualMachineSnapshotContent create_namespaced_virtual_machine_snapshot_content(body, namespace)



Create a VirtualMachineSnapshotContent object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1beta1VirtualMachineSnapshotContent() # V1beta1VirtualMachineSnapshotContent | 
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.create_namespaced_virtual_machine_snapshot_content(body, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1VirtualMachineSnapshotContent**](V1beta1VirtualMachineSnapshotContent.md)|  | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1beta1VirtualMachineSnapshotContent**](V1beta1VirtualMachineSnapshotContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_machine_clone**
> V1alpha1VirtualMachineClone create_virtual_machine_clone(body)



Create a VirtualMachineClone object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1alpha1VirtualMachineClone() # V1alpha1VirtualMachineClone | 

try: 
    api_response = api_instance.create_virtual_machine_clone(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_virtual_machine_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1VirtualMachineClone**](V1alpha1VirtualMachineClone.md)|  | 

### Return type

[**V1alpha1VirtualMachineClone**](V1alpha1VirtualMachineClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_machine_cluster_instancetype**
> V1beta1VirtualMachineClusterInstancetype create_virtual_machine_cluster_instancetype(body)



Create a VirtualMachineClusterInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1beta1VirtualMachineClusterInstancetype() # V1beta1VirtualMachineClusterInstancetype | 

try: 
    api_response = api_instance.create_virtual_machine_cluster_instancetype(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_virtual_machine_cluster_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1VirtualMachineClusterInstancetype**](V1beta1VirtualMachineClusterInstancetype.md)|  | 

### Return type

[**V1beta1VirtualMachineClusterInstancetype**](V1beta1VirtualMachineClusterInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_machine_cluster_preference**
> V1beta1VirtualMachineClusterPreference create_virtual_machine_cluster_preference(body)



Create a VirtualMachineClusterPreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
body = kubevirt.V1beta1VirtualMachineClusterPreference() # V1beta1VirtualMachineClusterPreference | 

try: 
    api_response = api_instance.create_virtual_machine_cluster_preference(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_virtual_machine_cluster_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1VirtualMachineClusterPreference**](V1beta1VirtualMachineClusterPreference.md)|  | 

### Return type

[**V1beta1VirtualMachineClusterPreference**](V1beta1VirtualMachineClusterPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_migration_policy**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_migration_policy(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of MigrationPolicy objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_migration_policy(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_migration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_kube_virt**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_kube_virt(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of KubeVirt objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_kube_virt(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachine objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_export**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_export(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineExport objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_export(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_instance**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_instance(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineInstance objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_instance(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_instance_migration**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_instance_migration(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineInstanceMigration objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_instance_migration(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_instance_preset**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_instance_preset(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineInstancePreset objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_instance_preset(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_instance_replica_set**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_instance_replica_set(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineInstanceReplicaSet objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_instance_replica_set(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_instancetype**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_instancetype(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineInstancetype objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_instancetype(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_pool**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_pool(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachinePool objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_pool(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_preference**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_preference(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachinePreference objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_preference(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_restore**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_restore(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineRestore objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_restore(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_snapshot**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_snapshot(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineSnapshot objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_snapshot(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_virtual_machine_snapshot_content**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_namespaced_virtual_machine_snapshot_content(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineSnapshotContent objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_virtual_machine_snapshot_content(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_virtual_machine_clone**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_virtual_machine_clone(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineClone objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_virtual_machine_clone(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_virtual_machine_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_virtual_machine_cluster_instancetype**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_virtual_machine_cluster_instancetype(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineClusterInstancetype objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_virtual_machine_cluster_instancetype(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_virtual_machine_cluster_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_virtual_machine_cluster_preference**
> K8sIoApimachineryPkgApisMetaV1Status delete_collection_virtual_machine_cluster_preference(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Delete a collection of VirtualMachineClusterPreference objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_virtual_machine_cluster_preference(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_collection_virtual_machine_cluster_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_migration_policy**
> K8sIoApimachineryPkgApisMetaV1Status delete_migration_policy(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a MigrationPolicy object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_migration_policy(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_migration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_kube_virt**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_kube_virt(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a KubeVirt object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_kube_virt(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_export**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_export(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineExport object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_export(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_instance**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_instance(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_instance(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_instance_migration**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_instance_migration(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineInstanceMigration object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_instance_migration(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_instance_preset**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_instance_preset(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineInstancePreset object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_instance_preset(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_instance_replica_set**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_instance_replica_set(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineInstanceReplicaSet object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_instance_replica_set(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_instancetype**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_instancetype(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_instancetype(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_pool**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_pool(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachinePool object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_pool(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_preference**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_preference(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachinePreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_preference(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_restore**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_restore(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineRestore object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_restore(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_snapshot**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_snapshot(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineSnapshot object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_snapshot(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_virtual_machine_snapshot_content**
> K8sIoApimachineryPkgApisMetaV1Status delete_namespaced_virtual_machine_snapshot_content(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineSnapshotContent object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_namespaced_virtual_machine_snapshot_content(name, namespace, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_machine_clone**
> K8sIoApimachineryPkgApisMetaV1Status delete_virtual_machine_clone(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineClone object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_virtual_machine_clone(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_virtual_machine_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_machine_cluster_instancetype**
> K8sIoApimachineryPkgApisMetaV1Status delete_virtual_machine_cluster_instancetype(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineClusterInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_virtual_machine_cluster_instancetype(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_virtual_machine_cluster_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_machine_cluster_preference**
> K8sIoApimachineryPkgApisMetaV1Status delete_virtual_machine_cluster_preference(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Delete a VirtualMachineClusterPreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1DeleteOptions() # K8sIoApimachineryPkgApisMetaV1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)

try: 
    api_response = api_instance.delete_virtual_machine_cluster_preference(name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_virtual_machine_cluster_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1DeleteOptions**](K8sIoApimachineryPkgApisMetaV1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1Status**](K8sIoApimachineryPkgApisMetaV1Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func13**
> func13()



Health endpoint

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.func13()
except ApiException as e:
    print("Exception when calling DefaultApi->func13: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **func6**
> func6()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.func6()
except ApiException as e:
    print("Exception when calling DefaultApi->func6: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_clone_kubevirt_io**
> K8sIoApimachineryPkgApisMetaV1APIGroup get_api_group_clone_kubevirt_io()



Get a KubeVirt API group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_clone_kubevirt_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_clone_kubevirt_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_export_kubevirt_io**
> K8sIoApimachineryPkgApisMetaV1APIGroup get_api_group_export_kubevirt_io()



Get a KubeVirt API group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_export_kubevirt_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_export_kubevirt_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_instancetype_kubevirt_io**
> K8sIoApimachineryPkgApisMetaV1APIGroup get_api_group_instancetype_kubevirt_io()



Get a KubeVirt API group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_instancetype_kubevirt_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_instancetype_kubevirt_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_kubevirt_io**
> K8sIoApimachineryPkgApisMetaV1APIGroup get_api_group_kubevirt_io()



Get a KubeVirt API group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_kubevirt_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_kubevirt_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_list**
> K8sIoApimachineryPkgApisMetaV1APIGroupList get_api_group_list()



Get a KubeVirt API GroupList

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroupList**](K8sIoApimachineryPkgApisMetaV1APIGroupList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_migrations_kubevirt_io**
> K8sIoApimachineryPkgApisMetaV1APIGroup get_api_group_migrations_kubevirt_io()



Get a KubeVirt API group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_migrations_kubevirt_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_migrations_kubevirt_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_pool_kubevirt_io**
> K8sIoApimachineryPkgApisMetaV1APIGroup get_api_group_pool_kubevirt_io()



Get a KubeVirt API group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_pool_kubevirt_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_pool_kubevirt_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_group_snapshot_kubevirt_io**
> K8sIoApimachineryPkgApisMetaV1APIGroup get_api_group_snapshot_kubevirt_io()



Get a KubeVirt API group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_group_snapshot_kubevirt_io()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_group_snapshot_kubevirt_io: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources_clone_kubevirt_io_v1alpha1**
> K8sIoApimachineryPkgApisMetaV1APIResourceList get_api_resources_clone_kubevirt_io_v1alpha1()



Get KubeVirt API Resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_resources_clone_kubevirt_io_v1alpha1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources_clone_kubevirt_io_v1alpha1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources_export_kubevirt_io_v1alpha1**
> K8sIoApimachineryPkgApisMetaV1APIResourceList get_api_resources_export_kubevirt_io_v1alpha1()



Get KubeVirt API Resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_resources_export_kubevirt_io_v1alpha1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources_export_kubevirt_io_v1alpha1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources_instancetype_kubevirt_io_v1beta1**
> K8sIoApimachineryPkgApisMetaV1APIResourceList get_api_resources_instancetype_kubevirt_io_v1beta1()



Get KubeVirt API Resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_resources_instancetype_kubevirt_io_v1beta1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources_instancetype_kubevirt_io_v1beta1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources_kubevirt_io_v1**
> K8sIoApimachineryPkgApisMetaV1APIResourceList get_api_resources_kubevirt_io_v1()



Get KubeVirt API Resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_resources_kubevirt_io_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources_kubevirt_io_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources_migrations_kubevirt_io_v1alpha1**
> K8sIoApimachineryPkgApisMetaV1APIResourceList get_api_resources_migrations_kubevirt_io_v1alpha1()



Get KubeVirt API Resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_resources_migrations_kubevirt_io_v1alpha1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources_migrations_kubevirt_io_v1alpha1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources_pool_kubevirt_io_v1alpha1**
> K8sIoApimachineryPkgApisMetaV1APIResourceList get_api_resources_pool_kubevirt_io_v1alpha1()



Get KubeVirt API Resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_resources_pool_kubevirt_io_v1alpha1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources_pool_kubevirt_io_v1alpha1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources_snapshot_kubevirt_io_v1beta1**
> K8sIoApimachineryPkgApisMetaV1APIResourceList get_api_resources_snapshot_kubevirt_io_v1beta1()



Get KubeVirt API Resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_api_resources_snapshot_kubevirt_io_v1beta1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_api_resources_snapshot_kubevirt_io_v1beta1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root_paths**
> K8sIoApimachineryPkgApisMetaV1RootPaths get_root_paths()



Get KubeVirt API root paths

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.get_root_paths()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_root_paths: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1RootPaths**](K8sIoApimachineryPkgApisMetaV1RootPaths.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_dump_profiler**
> handle_dump_profiler()



dump profiler results endpoint

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.handle_dump_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->handle_dump_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_start_profiler**
> handle_start_profiler()



start profiler endpoint

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.handle_start_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->handle_start_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_stop_profiler**
> handle_stop_profiler()



stop profiler endpoint

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.handle_stop_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->handle_stop_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kube_virt_for_all_namespaces**
> V1KubeVirtList list_kube_virt_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all KubeVirt objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_kube_virt_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_kube_virt_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1KubeVirtList**](V1KubeVirtList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_migration_policy**
> V1alpha1MigrationPolicyList list_migration_policy(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of MigrationPolicy objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_migration_policy(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_migration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1MigrationPolicyList**](V1alpha1MigrationPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_kube_virt**
> V1KubeVirtList list_namespaced_kube_virt(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of KubeVirt objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_kube_virt(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1KubeVirtList**](V1KubeVirtList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine**
> V1VirtualMachineList list_namespaced_virtual_machine(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachine objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineList**](V1VirtualMachineList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_export**
> V1alpha1VirtualMachineExportList list_namespaced_virtual_machine_export(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineExport objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_export(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1VirtualMachineExportList**](V1alpha1VirtualMachineExportList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_instance**
> V1VirtualMachineInstanceList list_namespaced_virtual_machine_instance(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineInstance objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_instance(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstanceList**](V1VirtualMachineInstanceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_instance_migration**
> V1VirtualMachineInstanceMigrationList list_namespaced_virtual_machine_instance_migration(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineInstanceMigration objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_instance_migration(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstanceMigrationList**](V1VirtualMachineInstanceMigrationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_instance_preset**
> V1VirtualMachineInstancePresetList list_namespaced_virtual_machine_instance_preset(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineInstancePreset objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_instance_preset(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstancePresetList**](V1VirtualMachineInstancePresetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_instance_replica_set**
> V1VirtualMachineInstanceReplicaSetList list_namespaced_virtual_machine_instance_replica_set(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineInstanceReplicaSet objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_instance_replica_set(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstanceReplicaSetList**](V1VirtualMachineInstanceReplicaSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_instancetype**
> V1beta1VirtualMachineInstancetypeList list_namespaced_virtual_machine_instancetype(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineInstancetype objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_instancetype(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineInstancetypeList**](V1beta1VirtualMachineInstancetypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_pool**
> V1alpha1VirtualMachinePoolList list_namespaced_virtual_machine_pool(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachinePool objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_pool(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1VirtualMachinePoolList**](V1alpha1VirtualMachinePoolList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_preference**
> V1beta1VirtualMachinePreferenceList list_namespaced_virtual_machine_preference(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachinePreference objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_preference(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachinePreferenceList**](V1beta1VirtualMachinePreferenceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_restore**
> V1beta1VirtualMachineRestoreList list_namespaced_virtual_machine_restore(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineRestore objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_restore(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineRestoreList**](V1beta1VirtualMachineRestoreList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_snapshot**
> V1beta1VirtualMachineSnapshotList list_namespaced_virtual_machine_snapshot(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineSnapshot objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_snapshot(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineSnapshotList**](V1beta1VirtualMachineSnapshotList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_virtual_machine_snapshot_content**
> V1beta1VirtualMachineSnapshotContentList list_namespaced_virtual_machine_snapshot_content(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineSnapshotContent objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_virtual_machine_snapshot_content(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineSnapshotContentList**](V1beta1VirtualMachineSnapshotContentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_clone**
> V1alpha1VirtualMachineCloneList list_virtual_machine_clone(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineClone objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_clone(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1VirtualMachineCloneList**](V1alpha1VirtualMachineCloneList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_cluster_instancetype**
> V1beta1VirtualMachineClusterInstancetypeList list_virtual_machine_cluster_instancetype(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineClusterInstancetype objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_cluster_instancetype(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_cluster_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineClusterInstancetypeList**](V1beta1VirtualMachineClusterInstancetypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_cluster_preference**
> V1beta1VirtualMachineClusterPreferenceList list_virtual_machine_cluster_preference(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of VirtualMachineClusterPreference objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_cluster_preference(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_cluster_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineClusterPreferenceList**](V1beta1VirtualMachineClusterPreferenceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_export_for_all_namespaces**
> V1alpha1VirtualMachineExportList list_virtual_machine_export_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineExport objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_export_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_export_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1VirtualMachineExportList**](V1alpha1VirtualMachineExportList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_for_all_namespaces**
> V1VirtualMachineList list_virtual_machine_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachine objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineList**](V1VirtualMachineList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_instance_for_all_namespaces**
> V1VirtualMachineInstanceList list_virtual_machine_instance_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineInstance objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_instance_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_instance_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstanceList**](V1VirtualMachineInstanceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_instance_migration_for_all_namespaces**
> V1VirtualMachineInstanceMigrationList list_virtual_machine_instance_migration_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineInstanceMigration objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_instance_migration_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_instance_migration_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstanceMigrationList**](V1VirtualMachineInstanceMigrationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_instance_preset_for_all_namespaces**
> V1VirtualMachineInstancePresetList list_virtual_machine_instance_preset_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineInstancePreset objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_instance_preset_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_instance_preset_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstancePresetList**](V1VirtualMachineInstancePresetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_instance_replica_set_for_all_namespaces**
> V1VirtualMachineInstanceReplicaSetList list_virtual_machine_instance_replica_set_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineInstanceReplicaSet objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_instance_replica_set_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_instance_replica_set_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1VirtualMachineInstanceReplicaSetList**](V1VirtualMachineInstanceReplicaSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_instancetype_for_all_namespaces**
> V1beta1VirtualMachineInstancetypeList list_virtual_machine_instancetype_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineInstancetype objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_instancetype_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_instancetype_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineInstancetypeList**](V1beta1VirtualMachineInstancetypeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_pool_for_all_namespaces**
> V1alpha1VirtualMachinePoolList list_virtual_machine_pool_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachinePool objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_pool_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_pool_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1VirtualMachinePoolList**](V1alpha1VirtualMachinePoolList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_preference_for_all_namespaces**
> V1beta1VirtualMachinePreferenceList list_virtual_machine_preference_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachinePreference objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_preference_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_preference_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachinePreferenceList**](V1beta1VirtualMachinePreferenceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_restore_for_all_namespaces**
> V1beta1VirtualMachineRestoreList list_virtual_machine_restore_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineRestore objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_restore_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_restore_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineRestoreList**](V1beta1VirtualMachineRestoreList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_snapshot_content_for_all_namespaces**
> V1beta1VirtualMachineSnapshotContentList list_virtual_machine_snapshot_content_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineSnapshotContent objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_snapshot_content_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_snapshot_content_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineSnapshotContentList**](V1beta1VirtualMachineSnapshotContentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_machine_snapshot_for_all_namespaces**
> V1beta1VirtualMachineSnapshotList list_virtual_machine_snapshot_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Get a list of all VirtualMachineSnapshot objects.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_virtual_machine_snapshot_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_virtual_machine_snapshot_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1VirtualMachineSnapshotList**](V1beta1VirtualMachineSnapshotList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_migration_policy**
> V1alpha1MigrationPolicy patch_migration_policy(name, body)



Patch a MigrationPolicy object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_migration_policy(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_migration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1alpha1MigrationPolicy**](V1alpha1MigrationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_kube_virt**
> V1KubeVirt patch_namespaced_kube_virt(name, namespace, body)



Patch a KubeVirt object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_kube_virt(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1KubeVirt**](V1KubeVirt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine**
> V1VirtualMachine patch_namespaced_virtual_machine(name, namespace, body)



Patch a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_export**
> V1alpha1VirtualMachineExport patch_namespaced_virtual_machine_export(name, namespace, body)



Patch a VirtualMachineExport object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_export(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1alpha1VirtualMachineExport**](V1alpha1VirtualMachineExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_instance**
> V1VirtualMachineInstance patch_namespaced_virtual_machine_instance(name, namespace, body)



Patch a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_instance(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1VirtualMachineInstance**](V1VirtualMachineInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_instance_migration**
> V1VirtualMachineInstanceMigration patch_namespaced_virtual_machine_instance_migration(name, namespace, body)



Patch a VirtualMachineInstanceMigration object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_instance_migration(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1VirtualMachineInstanceMigration**](V1VirtualMachineInstanceMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_instance_preset**
> V1VirtualMachineInstancePreset patch_namespaced_virtual_machine_instance_preset(name, namespace, body)



Patch a VirtualMachineInstancePreset object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_instance_preset(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1VirtualMachineInstancePreset**](V1VirtualMachineInstancePreset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_instance_replica_set**
> V1VirtualMachineInstanceReplicaSet patch_namespaced_virtual_machine_instance_replica_set(name, namespace, body)



Patch a VirtualMachineInstanceReplicaSet object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_instance_replica_set(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1VirtualMachineInstanceReplicaSet**](V1VirtualMachineInstanceReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_instancetype**
> V1beta1VirtualMachineInstancetype patch_namespaced_virtual_machine_instancetype(name, namespace, body)



Patch a VirtualMachineInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_instancetype(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1beta1VirtualMachineInstancetype**](V1beta1VirtualMachineInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_pool**
> V1alpha1VirtualMachinePool patch_namespaced_virtual_machine_pool(name, namespace, body)



Patch a VirtualMachinePool object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_pool(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1alpha1VirtualMachinePool**](V1alpha1VirtualMachinePool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_preference**
> V1beta1VirtualMachinePreference patch_namespaced_virtual_machine_preference(name, namespace, body)



Patch a VirtualMachinePreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_preference(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1beta1VirtualMachinePreference**](V1beta1VirtualMachinePreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_restore**
> V1beta1VirtualMachineRestore patch_namespaced_virtual_machine_restore(name, namespace, body)



Patch a VirtualMachineRestore object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_restore(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1beta1VirtualMachineRestore**](V1beta1VirtualMachineRestore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_snapshot**
> V1beta1VirtualMachineSnapshot patch_namespaced_virtual_machine_snapshot(name, namespace, body)



Patch a VirtualMachineSnapshot object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_snapshot(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1beta1VirtualMachineSnapshot**](V1beta1VirtualMachineSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_virtual_machine_snapshot_content**
> V1beta1VirtualMachineSnapshotContent patch_namespaced_virtual_machine_snapshot_content(name, namespace, body)



Patch a VirtualMachineSnapshotContent object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_namespaced_virtual_machine_snapshot_content(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1beta1VirtualMachineSnapshotContent**](V1beta1VirtualMachineSnapshotContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_virtual_machine_clone**
> V1alpha1VirtualMachineClone patch_virtual_machine_clone(name, body)



Patch a VirtualMachineClone object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_virtual_machine_clone(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_virtual_machine_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1alpha1VirtualMachineClone**](V1alpha1VirtualMachineClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_virtual_machine_cluster_instancetype**
> V1beta1VirtualMachineClusterInstancetype patch_virtual_machine_cluster_instancetype(name, body)



Patch a VirtualMachineClusterInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_virtual_machine_cluster_instancetype(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_virtual_machine_cluster_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1beta1VirtualMachineClusterInstancetype**](V1beta1VirtualMachineClusterInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_virtual_machine_cluster_preference**
> V1beta1VirtualMachineClusterPreference patch_virtual_machine_cluster_preference(name, body)



Patch a VirtualMachineClusterPreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.K8sIoApimachineryPkgApisMetaV1Patch() # K8sIoApimachineryPkgApisMetaV1Patch | 

try: 
    api_response = api_instance.patch_virtual_machine_cluster_preference(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->patch_virtual_machine_cluster_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**K8sIoApimachineryPkgApisMetaV1Patch**](K8sIoApimachineryPkgApisMetaV1Patch.md)|  | 

### Return type

[**V1beta1VirtualMachineClusterPreference**](V1beta1VirtualMachineClusterPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_migration_policy**
> V1alpha1MigrationPolicy read_migration_policy(name, exact=exact, export=export)



Get a MigrationPolicy object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_migration_policy(name, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_migration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1alpha1MigrationPolicy**](V1alpha1MigrationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_kube_virt**
> V1KubeVirt read_namespaced_kube_virt(name, namespace, exact=exact, export=export)



Get a KubeVirt object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_kube_virt(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1KubeVirt**](V1KubeVirt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine**
> V1VirtualMachine read_namespaced_virtual_machine(name, namespace, exact=exact, export=export)



Get a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_export**
> V1alpha1VirtualMachineExport read_namespaced_virtual_machine_export(name, namespace, exact=exact, export=export)



Get a VirtualMachineExport object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_export(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1alpha1VirtualMachineExport**](V1alpha1VirtualMachineExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_instance**
> V1VirtualMachineInstance read_namespaced_virtual_machine_instance(name, namespace, exact=exact, export=export)



Get a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_instance(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1VirtualMachineInstance**](V1VirtualMachineInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_instance_migration**
> V1VirtualMachineInstanceMigration read_namespaced_virtual_machine_instance_migration(name, namespace, exact=exact, export=export)



Get a VirtualMachineInstanceMigration object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_instance_migration(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1VirtualMachineInstanceMigration**](V1VirtualMachineInstanceMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_instance_preset**
> V1VirtualMachineInstancePreset read_namespaced_virtual_machine_instance_preset(name, namespace, exact=exact, export=export)



Get a VirtualMachineInstancePreset object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_instance_preset(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1VirtualMachineInstancePreset**](V1VirtualMachineInstancePreset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_instance_replica_set**
> V1VirtualMachineInstanceReplicaSet read_namespaced_virtual_machine_instance_replica_set(name, namespace, exact=exact, export=export)



Get a VirtualMachineInstanceReplicaSet object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_instance_replica_set(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1VirtualMachineInstanceReplicaSet**](V1VirtualMachineInstanceReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_instancetype**
> V1beta1VirtualMachineInstancetype read_namespaced_virtual_machine_instancetype(name, namespace, exact=exact, export=export)



Get a VirtualMachineInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_instancetype(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1VirtualMachineInstancetype**](V1beta1VirtualMachineInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_pool**
> V1alpha1VirtualMachinePool read_namespaced_virtual_machine_pool(name, namespace, exact=exact, export=export)



Get a VirtualMachinePool object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_pool(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1alpha1VirtualMachinePool**](V1alpha1VirtualMachinePool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_preference**
> V1beta1VirtualMachinePreference read_namespaced_virtual_machine_preference(name, namespace, exact=exact, export=export)



Get a VirtualMachinePreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_preference(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1VirtualMachinePreference**](V1beta1VirtualMachinePreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_restore**
> V1beta1VirtualMachineRestore read_namespaced_virtual_machine_restore(name, namespace, exact=exact, export=export)



Get a VirtualMachineRestore object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_restore(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1VirtualMachineRestore**](V1beta1VirtualMachineRestore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_snapshot**
> V1beta1VirtualMachineSnapshot read_namespaced_virtual_machine_snapshot(name, namespace, exact=exact, export=export)



Get a VirtualMachineSnapshot object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_snapshot(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1VirtualMachineSnapshot**](V1beta1VirtualMachineSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_virtual_machine_snapshot_content**
> V1beta1VirtualMachineSnapshotContent read_namespaced_virtual_machine_snapshot_content(name, namespace, exact=exact, export=export)



Get a VirtualMachineSnapshotContent object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_virtual_machine_snapshot_content(name, namespace, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1VirtualMachineSnapshotContent**](V1beta1VirtualMachineSnapshotContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_virtual_machine_clone**
> V1alpha1VirtualMachineClone read_virtual_machine_clone(name, exact=exact, export=export)



Get a VirtualMachineClone object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_virtual_machine_clone(name, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_virtual_machine_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1alpha1VirtualMachineClone**](V1alpha1VirtualMachineClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_virtual_machine_cluster_instancetype**
> V1beta1VirtualMachineClusterInstancetype read_virtual_machine_cluster_instancetype(name, exact=exact, export=export)



Get a VirtualMachineClusterInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_virtual_machine_cluster_instancetype(name, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_virtual_machine_cluster_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1VirtualMachineClusterInstancetype**](V1beta1VirtualMachineClusterInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_virtual_machine_cluster_preference**
> V1beta1VirtualMachineClusterPreference read_virtual_machine_cluster_preference(name, exact=exact, export=export)



Get a VirtualMachineClusterPreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
exact = true # bool | Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported. Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_virtual_machine_cluster_preference(name, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->read_virtual_machine_cluster_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **exact** | **bool**| Should the export be exact. Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported. Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1VirtualMachineClusterPreference**](V1beta1VirtualMachineClusterPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_migration_policy**
> V1alpha1MigrationPolicy replace_migration_policy(name, body)



Update a MigrationPolicy object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.V1alpha1MigrationPolicy() # V1alpha1MigrationPolicy | 

try: 
    api_response = api_instance.replace_migration_policy(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_migration_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**V1alpha1MigrationPolicy**](V1alpha1MigrationPolicy.md)|  | 

### Return type

[**V1alpha1MigrationPolicy**](V1alpha1MigrationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_kube_virt**
> V1KubeVirt replace_namespaced_kube_virt(name, namespace, body)



Update a KubeVirt object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1KubeVirt() # V1KubeVirt | 

try: 
    api_response = api_instance.replace_namespaced_kube_virt(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1KubeVirt**](V1KubeVirt.md)|  | 

### Return type

[**V1KubeVirt**](V1KubeVirt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine**
> V1VirtualMachine replace_namespaced_virtual_machine(name, namespace, body)



Update a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1VirtualMachine() # V1VirtualMachine | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1VirtualMachine**](V1VirtualMachine.md)|  | 

### Return type

[**V1VirtualMachine**](V1VirtualMachine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_export**
> V1alpha1VirtualMachineExport replace_namespaced_virtual_machine_export(name, namespace, body)



Update a VirtualMachineExport object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1alpha1VirtualMachineExport() # V1alpha1VirtualMachineExport | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_export(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1VirtualMachineExport**](V1alpha1VirtualMachineExport.md)|  | 

### Return type

[**V1alpha1VirtualMachineExport**](V1alpha1VirtualMachineExport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_instance**
> V1VirtualMachineInstance replace_namespaced_virtual_machine_instance(name, namespace, body)



Update a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1VirtualMachineInstance() # V1VirtualMachineInstance | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_instance(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1VirtualMachineInstance**](V1VirtualMachineInstance.md)|  | 

### Return type

[**V1VirtualMachineInstance**](V1VirtualMachineInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_instance_migration**
> V1VirtualMachineInstanceMigration replace_namespaced_virtual_machine_instance_migration(name, namespace, body)



Update a VirtualMachineInstanceMigration object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1VirtualMachineInstanceMigration() # V1VirtualMachineInstanceMigration | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_instance_migration(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1VirtualMachineInstanceMigration**](V1VirtualMachineInstanceMigration.md)|  | 

### Return type

[**V1VirtualMachineInstanceMigration**](V1VirtualMachineInstanceMigration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_instance_preset**
> V1VirtualMachineInstancePreset replace_namespaced_virtual_machine_instance_preset(name, namespace, body)



Update a VirtualMachineInstancePreset object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1VirtualMachineInstancePreset() # V1VirtualMachineInstancePreset | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_instance_preset(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1VirtualMachineInstancePreset**](V1VirtualMachineInstancePreset.md)|  | 

### Return type

[**V1VirtualMachineInstancePreset**](V1VirtualMachineInstancePreset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_instance_replica_set**
> V1VirtualMachineInstanceReplicaSet replace_namespaced_virtual_machine_instance_replica_set(name, namespace, body)



Update a VirtualMachineInstanceReplicaSet object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1VirtualMachineInstanceReplicaSet() # V1VirtualMachineInstanceReplicaSet | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_instance_replica_set(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1VirtualMachineInstanceReplicaSet**](V1VirtualMachineInstanceReplicaSet.md)|  | 

### Return type

[**V1VirtualMachineInstanceReplicaSet**](V1VirtualMachineInstanceReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_instancetype**
> V1beta1VirtualMachineInstancetype replace_namespaced_virtual_machine_instancetype(name, namespace, body)



Update a VirtualMachineInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1beta1VirtualMachineInstancetype() # V1beta1VirtualMachineInstancetype | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_instancetype(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1VirtualMachineInstancetype**](V1beta1VirtualMachineInstancetype.md)|  | 

### Return type

[**V1beta1VirtualMachineInstancetype**](V1beta1VirtualMachineInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_pool**
> V1alpha1VirtualMachinePool replace_namespaced_virtual_machine_pool(name, namespace, body)



Update a VirtualMachinePool object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1alpha1VirtualMachinePool() # V1alpha1VirtualMachinePool | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_pool(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1VirtualMachinePool**](V1alpha1VirtualMachinePool.md)|  | 

### Return type

[**V1alpha1VirtualMachinePool**](V1alpha1VirtualMachinePool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_preference**
> V1beta1VirtualMachinePreference replace_namespaced_virtual_machine_preference(name, namespace, body)



Update a VirtualMachinePreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1beta1VirtualMachinePreference() # V1beta1VirtualMachinePreference | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_preference(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1VirtualMachinePreference**](V1beta1VirtualMachinePreference.md)|  | 

### Return type

[**V1beta1VirtualMachinePreference**](V1beta1VirtualMachinePreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_restore**
> V1beta1VirtualMachineRestore replace_namespaced_virtual_machine_restore(name, namespace, body)



Update a VirtualMachineRestore object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1beta1VirtualMachineRestore() # V1beta1VirtualMachineRestore | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_restore(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1VirtualMachineRestore**](V1beta1VirtualMachineRestore.md)|  | 

### Return type

[**V1beta1VirtualMachineRestore**](V1beta1VirtualMachineRestore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_snapshot**
> V1beta1VirtualMachineSnapshot replace_namespaced_virtual_machine_snapshot(name, namespace, body)



Update a VirtualMachineSnapshot object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1beta1VirtualMachineSnapshot() # V1beta1VirtualMachineSnapshot | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_snapshot(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1VirtualMachineSnapshot**](V1beta1VirtualMachineSnapshot.md)|  | 

### Return type

[**V1beta1VirtualMachineSnapshot**](V1beta1VirtualMachineSnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_virtual_machine_snapshot_content**
> V1beta1VirtualMachineSnapshotContent replace_namespaced_virtual_machine_snapshot_content(name, namespace, body)



Update a VirtualMachineSnapshotContent object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1beta1VirtualMachineSnapshotContent() # V1beta1VirtualMachineSnapshotContent | 

try: 
    api_response = api_instance.replace_namespaced_virtual_machine_snapshot_content(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1VirtualMachineSnapshotContent**](V1beta1VirtualMachineSnapshotContent.md)|  | 

### Return type

[**V1beta1VirtualMachineSnapshotContent**](V1beta1VirtualMachineSnapshotContent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_virtual_machine_clone**
> V1alpha1VirtualMachineClone replace_virtual_machine_clone(name, body)



Update a VirtualMachineClone object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.V1alpha1VirtualMachineClone() # V1alpha1VirtualMachineClone | 

try: 
    api_response = api_instance.replace_virtual_machine_clone(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_virtual_machine_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**V1alpha1VirtualMachineClone**](V1alpha1VirtualMachineClone.md)|  | 

### Return type

[**V1alpha1VirtualMachineClone**](V1alpha1VirtualMachineClone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_virtual_machine_cluster_instancetype**
> V1beta1VirtualMachineClusterInstancetype replace_virtual_machine_cluster_instancetype(name, body)



Update a VirtualMachineClusterInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.V1beta1VirtualMachineClusterInstancetype() # V1beta1VirtualMachineClusterInstancetype | 

try: 
    api_response = api_instance.replace_virtual_machine_cluster_instancetype(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_virtual_machine_cluster_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**V1beta1VirtualMachineClusterInstancetype**](V1beta1VirtualMachineClusterInstancetype.md)|  | 

### Return type

[**V1beta1VirtualMachineClusterInstancetype**](V1beta1VirtualMachineClusterInstancetype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_virtual_machine_cluster_preference**
> V1beta1VirtualMachineClusterPreference replace_virtual_machine_cluster_preference(name, body)



Update a VirtualMachineClusterPreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
body = kubevirt.V1beta1VirtualMachineClusterPreference() # V1beta1VirtualMachineClusterPreference | 

try: 
    api_response = api_instance.replace_virtual_machine_cluster_preference(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->replace_virtual_machine_cluster_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **body** | [**V1beta1VirtualMachineClusterPreference**](V1beta1VirtualMachineClusterPreference.md)|  | 

### Return type

[**V1beta1VirtualMachineClusterPreference**](V1beta1VirtualMachineClusterPreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_check_health**
> str v1_check_health()



Health endpoint

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.v1_check_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_check_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_console**
> v1_console(name, namespace)



Open a websocket connection to a serial console on the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_instance.v1_console(name, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_console: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_expand_spec**
> str v1_expand_spec(namespace)



Expands instancetype and preference into the passed VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_expand_spec(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_expand_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_filesystemlist**
> V1VirtualMachineInstanceFileSystemList v1_filesystemlist(name, namespace)



Get list of active filesystems on guest machine via guest agent

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_filesystemlist(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_filesystemlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceFileSystemList**](V1VirtualMachineInstanceFileSystemList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_freeze**
> str v1_freeze(name, namespace, body)



Freeze a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1FreezeUnfreezeTimeout() # V1FreezeUnfreezeTimeout | 

try: 
    api_response = api_instance.v1_freeze(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1FreezeUnfreezeTimeout**](V1FreezeUnfreezeTimeout.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_sub_api_group**
> K8sIoApimachineryPkgApisMetaV1APIGroup v1_get_sub_api_group()



Get a KubeVirt API Group

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.v1_get_sub_api_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_get_sub_api_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIGroup**](K8sIoApimachineryPkgApisMetaV1APIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_guestfs**
> str v1_guestfs()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.v1_guestfs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_guestfs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_guestosinfo**
> V1VirtualMachineInstanceGuestAgentInfo v1_guestosinfo(name, namespace)



Get guest agent os information

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_guestosinfo(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_guestosinfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceGuestAgentInfo**](V1VirtualMachineInstanceGuestAgentInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_memory_dump**
> str v1_memory_dump(name, namespace, body)



Dumps a VirtualMachineInstance memory.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1VirtualMachineMemoryDumpRequest() # V1VirtualMachineMemoryDumpRequest | 

try: 
    api_response = api_instance.v1_memory_dump(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_memory_dump: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1VirtualMachineMemoryDumpRequest**](V1VirtualMachineMemoryDumpRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_migrate**
> str v1_migrate(name, namespace, body)



Migrate a running VirtualMachine to another node.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1MigrateOptions() # V1MigrateOptions | 

try: 
    api_response = api_instance.v1_migrate(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_migrate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1MigrateOptions**](V1MigrateOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pause**
> str v1_pause(name, namespace, body)



Pause a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1PauseOptions() # V1PauseOptions | 

try: 
    api_response = api_instance.v1_pause(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1PauseOptions**](V1PauseOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_remove_memory_dump**
> str v1_remove_memory_dump(name, namespace)



Remove memory dump association.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_remove_memory_dump(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_remove_memory_dump: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_restart**
> str v1_restart(name, namespace, body=body)



Restart a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1RestartOptions() # V1RestartOptions |  (optional)

try: 
    api_response = api_instance.v1_restart(name, namespace, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1RestartOptions**](V1RestartOptions.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sev_fetch_cert_chain**
> V1SEVPlatformInfo v1_sev_fetch_cert_chain(name, namespace)



Fetch SEV certificate chain from the node where Virtual Machine is scheduled

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_sev_fetch_cert_chain(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_sev_fetch_cert_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1SEVPlatformInfo**](V1SEVPlatformInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sev_inject_launch_secret**
> str v1_sev_inject_launch_secret(name, namespace, body)



Inject SEV launch secret into a Virtual Machine

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1SEVSecretOptions() # V1SEVSecretOptions | 

try: 
    api_response = api_instance.v1_sev_inject_launch_secret(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_sev_inject_launch_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1SEVSecretOptions**](V1SEVSecretOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sev_query_launch_measurement**
> V1SEVMeasurementInfo v1_sev_query_launch_measurement(name, namespace)



Query SEV launch measurement from a Virtual Machine

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_sev_query_launch_measurement(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_sev_query_launch_measurement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1SEVMeasurementInfo**](V1SEVMeasurementInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_sev_setup_session**
> str v1_sev_setup_session(name, namespace, body)



Setup SEV session parameters for a Virtual Machine

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1SEVSessionOptions() # V1SEVSessionOptions | 

try: 
    api_response = api_instance.v1_sev_setup_session(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_sev_setup_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1SEVSessionOptions**](V1SEVSessionOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_soft_reboot**
> str v1_soft_reboot(name, namespace)



Soft reboot a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_soft_reboot(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_soft_reboot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_start**
> str v1_start(name, namespace, body)



Start a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1StartOptions() # V1StartOptions | 

try: 
    api_response = api_instance.v1_start(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1StartOptions**](V1StartOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stop**
> str v1_stop(name, namespace, body=body)



Stop a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1StopOptions() # V1StopOptions |  (optional)

try: 
    api_response = api_instance.v1_stop(name, namespace, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1StopOptions**](V1StopOptions.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_unfreeze**
> str v1_unfreeze(name, namespace)



Unfreeze a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_unfreeze(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_unfreeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_unpause**
> str v1_unpause(name, namespace, body)



Unpause a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1UnpauseOptions() # V1UnpauseOptions | 

try: 
    api_response = api_instance.v1_unpause(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_unpause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1UnpauseOptions**](V1UnpauseOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_userlist**
> V1VirtualMachineInstanceGuestOSUserList v1_userlist(name, namespace)



Get list of active users via guest agent

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1_userlist(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_userlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceGuestOSUserList**](V1VirtualMachineInstanceGuestOSUserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_version**
> v1_version()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1_version()
except ApiException as e:
    print("Exception when calling DefaultApi->v1_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vnc**
> v1_vnc(name, namespace)



Open a websocket connection to connect to VNC on the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_instance.v1_vnc(name, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_vnc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vnc_screenshot**
> v1_vnc_screenshot(name, namespace, move_cursor=move_cursor)



Get a PNG VNC screenshot of the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
move_cursor = true # bool | Move the cursor on the VNC display to wake up the screen (optional)

try: 
    api_instance.v1_vnc_screenshot(name, namespace, move_cursor=move_cursor)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_vnc_screenshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **move_cursor** | **bool**| Move the cursor on the VNC display to wake up the screen | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_vsock**
> v1_vsock(name, namespace, port, tls=tls)



Open a websocket connection forwarding traffic to the specified VirtualMachineInstance and port via VSOCK.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 56 # int | The port which the VSOCK application listens to.
tls = true # bool | Weather to request a TLS encrypted session from the VSOCK application. (optional)

try: 
    api_instance.v1_vsock(name, namespace, port, tls=tls)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_vsock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **int**| The port which the VSOCK application listens to. | 
 **tls** | **bool**| Weather to request a TLS encrypted session from the VSOCK application. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_check_health**
> str v1alpha3_check_health()



Health endpoint

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.v1alpha3_check_health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_check_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_console**
> v1alpha3_console(name, namespace)



Open a websocket connection to a serial console on the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_instance.v1alpha3_console(name, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_console: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_expand_spec**
> str v1alpha3_expand_spec(namespace)



Expands instancetype and preference into the passed VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_expand_spec(namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_expand_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_filesystemlist**
> V1VirtualMachineInstanceFileSystemList v1alpha3_filesystemlist(name, namespace)



Get list of active filesystems on guest machine via guest agent

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_filesystemlist(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_filesystemlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceFileSystemList**](V1VirtualMachineInstanceFileSystemList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_freeze**
> str v1alpha3_freeze(name, namespace, body)



Freeze a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1FreezeUnfreezeTimeout() # V1FreezeUnfreezeTimeout | 

try: 
    api_response = api_instance.v1alpha3_freeze(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_freeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1FreezeUnfreezeTimeout**](V1FreezeUnfreezeTimeout.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_guestfs**
> str v1alpha3_guestfs()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.v1alpha3_guestfs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_guestfs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_guestosinfo**
> V1VirtualMachineInstanceGuestAgentInfo v1alpha3_guestosinfo(name, namespace)



Get guest agent os information

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_guestosinfo(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_guestosinfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceGuestAgentInfo**](V1VirtualMachineInstanceGuestAgentInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_memory_dump**
> str v1alpha3_memory_dump(name, namespace, body)



Dumps a VirtualMachineInstance memory.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1VirtualMachineMemoryDumpRequest() # V1VirtualMachineMemoryDumpRequest | 

try: 
    api_response = api_instance.v1alpha3_memory_dump(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_memory_dump: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1VirtualMachineMemoryDumpRequest**](V1VirtualMachineMemoryDumpRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_migrate**
> str v1alpha3_migrate(name, namespace, body)



Migrate a running VirtualMachine to another node.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1MigrateOptions() # V1MigrateOptions | 

try: 
    api_response = api_instance.v1alpha3_migrate(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_migrate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1MigrateOptions**](V1MigrateOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_pause**
> str v1alpha3_pause(name, namespace, body)



Pause a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1PauseOptions() # V1PauseOptions | 

try: 
    api_response = api_instance.v1alpha3_pause(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1PauseOptions**](V1PauseOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_remove_memory_dump**
> str v1alpha3_remove_memory_dump(name, namespace)



Remove memory dump association.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_remove_memory_dump(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_remove_memory_dump: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_restart**
> str v1alpha3_restart(name, namespace, body=body)



Restart a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1RestartOptions() # V1RestartOptions |  (optional)

try: 
    api_response = api_instance.v1alpha3_restart(name, namespace, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1RestartOptions**](V1RestartOptions.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_sev_fetch_cert_chain**
> V1SEVPlatformInfo v1alpha3_sev_fetch_cert_chain(name, namespace)



Fetch SEV certificate chain from the node where Virtual Machine is scheduled

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_sev_fetch_cert_chain(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_sev_fetch_cert_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1SEVPlatformInfo**](V1SEVPlatformInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_sev_inject_launch_secret**
> str v1alpha3_sev_inject_launch_secret(name, namespace, body)



Inject SEV launch secret into a Virtual Machine

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1SEVSecretOptions() # V1SEVSecretOptions | 

try: 
    api_response = api_instance.v1alpha3_sev_inject_launch_secret(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_sev_inject_launch_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1SEVSecretOptions**](V1SEVSecretOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_sev_query_launch_measurement**
> V1SEVMeasurementInfo v1alpha3_sev_query_launch_measurement(name, namespace)



Query SEV launch measurement from a Virtual Machine

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_sev_query_launch_measurement(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_sev_query_launch_measurement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1SEVMeasurementInfo**](V1SEVMeasurementInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_sev_setup_session**
> str v1alpha3_sev_setup_session(name, namespace, body)



Setup SEV session parameters for a Virtual Machine

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1SEVSessionOptions() # V1SEVSessionOptions | 

try: 
    api_response = api_instance.v1alpha3_sev_setup_session(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_sev_setup_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1SEVSessionOptions**](V1SEVSessionOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_soft_reboot**
> str v1alpha3_soft_reboot(name, namespace)



Soft reboot a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_soft_reboot(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_soft_reboot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_start**
> str v1alpha3_start(name, namespace, body)



Start a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1StartOptions() # V1StartOptions | 

try: 
    api_response = api_instance.v1alpha3_start(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1StartOptions**](V1StartOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_stop**
> str v1alpha3_stop(name, namespace, body=body)



Stop a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1StopOptions() # V1StopOptions |  (optional)

try: 
    api_response = api_instance.v1alpha3_stop(name, namespace, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1StopOptions**](V1StopOptions.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_unfreeze**
> str v1alpha3_unfreeze(name, namespace)



Unfreeze a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_unfreeze(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_unfreeze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_unpause**
> str v1alpha3_unpause(name, namespace, body)



Unpause a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1UnpauseOptions() # V1UnpauseOptions | 

try: 
    api_response = api_instance.v1alpha3_unpause(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_unpause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1UnpauseOptions**](V1UnpauseOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_userlist**
> V1VirtualMachineInstanceGuestOSUserList v1alpha3_userlist(name, namespace)



Get list of active users via guest agent

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3_userlist(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_userlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

[**V1VirtualMachineInstanceGuestOSUserList**](V1VirtualMachineInstanceGuestOSUserList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_version**
> v1alpha3_version()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1alpha3_version()
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_vnc**
> v1alpha3_vnc(name, namespace)



Open a websocket connection to connect to VNC on the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_instance.v1alpha3_vnc(name, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_vnc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_vnc_screenshot**
> v1alpha3_vnc_screenshot(name, namespace, move_cursor=move_cursor)



Get a PNG VNC screenshot of the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
move_cursor = true # bool | Move the cursor on the VNC display to wake up the screen (optional)

try: 
    api_instance.v1alpha3_vnc_screenshot(name, namespace, move_cursor=move_cursor)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_vnc_screenshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **move_cursor** | **bool**| Move the cursor on the VNC display to wake up the screen | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3_vsock**
> v1alpha3_vsock(name, namespace, port, tls=tls)



Open a websocket connection forwarding traffic to the specified VirtualMachineInstance and port via VSOCK.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 56 # int | The port which the VSOCK application listens to.
tls = true # bool | Weather to request a TLS encrypted session from the VSOCK application. (optional)

try: 
    api_instance.v1alpha3_vsock(name, namespace, port, tls=tls)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3_vsock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **int**| The port which the VSOCK application listens to. | 
 **tls** | **bool**| Weather to request a TLS encrypted session from the VSOCK application. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3dump_cluster_profiler**
> v1alpha3dump_cluster_profiler()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1alpha3dump_cluster_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3dump_cluster_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3get_api_sub_resources**
> K8sIoApimachineryPkgApisMetaV1APIResourceList v1alpha3get_api_sub_resources()



Get a KubeVirt API resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.v1alpha3get_api_sub_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3get_api_sub_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3start_cluster_profiler**
> v1alpha3start_cluster_profiler()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1alpha3start_cluster_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3start_cluster_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3stop_cluster_profiler**
> v1alpha3stop_cluster_profiler()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1alpha3stop_cluster_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3stop_cluster_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3usbredir**
> v1alpha3usbredir(name, namespace)



Open a websocket connection to connect to USB device on the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_instance.v1alpha3usbredir(name, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3usbredir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vm_addvolume**
> str v1alpha3vm_addvolume(name, namespace, body)



Add a volume and disk to a running Virtual Machine.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1AddVolumeOptions() # V1AddVolumeOptions | 

try: 
    api_response = api_instance.v1alpha3vm_addvolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vm_addvolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1AddVolumeOptions**](V1AddVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vm_expand_spec**
> str v1alpha3vm_expand_spec(name, namespace)



Get VirtualMachine object with expanded instancetype and preference.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1alpha3vm_expand_spec(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vm_expand_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vm_port_forward**
> v1alpha3vm_port_forward(name, namespace, port)



Open a websocket connection forwarding traffic to the running VMI for the specified VirtualMachine and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1alpha3vm_port_forward(name, namespace, port)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vm_port_forward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vm_port_forward_with_protocol**
> v1alpha3vm_port_forward_with_protocol(name, namespace, port, protocol)



Open a websocket connection forwarding traffic of the specified protocol (either tcp or udp) to the specified VirtualMachine and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.
protocol = 'protocol_example' # str | The protocol for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1alpha3vm_port_forward_with_protocol(name, namespace, port, protocol)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vm_port_forward_with_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 
 **protocol** | **str**| The protocol for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vm_removevolume**
> str v1alpha3vm_removevolume(name, namespace, body)



Removes a volume and disk from a running Virtual Machine.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1RemoveVolumeOptions() # V1RemoveVolumeOptions | 

try: 
    api_response = api_instance.v1alpha3vm_removevolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vm_removevolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1RemoveVolumeOptions**](V1RemoveVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vmi_addvolume**
> str v1alpha3vmi_addvolume(name, namespace, body)



Add a volume and disk to a running Virtual Machine Instance

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1AddVolumeOptions() # V1AddVolumeOptions | 

try: 
    api_response = api_instance.v1alpha3vmi_addvolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vmi_addvolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1AddVolumeOptions**](V1AddVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vmi_port_forward**
> v1alpha3vmi_port_forward(name, namespace, port)



Open a websocket connection forwarding traffic to the specified VirtualMachineInstance and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1alpha3vmi_port_forward(name, namespace, port)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vmi_port_forward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vmi_port_forward_with_protocol**
> v1alpha3vmi_port_forward_with_protocol(name, namespace, port, protocol)



Open a websocket connection forwarding traffic of the specified protocol (either tcp or udp) to the specified VirtualMachineInstance and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.
protocol = 'protocol_example' # str | The protocol for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1alpha3vmi_port_forward_with_protocol(name, namespace, port, protocol)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vmi_port_forward_with_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 
 **protocol** | **str**| The protocol for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1alpha3vmi_removevolume**
> str v1alpha3vmi_removevolume(name, namespace, body)



Removes a volume and disk from a running Virtual Machine Instance

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1RemoveVolumeOptions() # V1RemoveVolumeOptions | 

try: 
    api_response = api_instance.v1alpha3vmi_removevolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1alpha3vmi_removevolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1RemoveVolumeOptions**](V1RemoveVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1dump_cluster_profiler**
> v1dump_cluster_profiler()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1dump_cluster_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->v1dump_cluster_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1get_api_sub_resources**
> K8sIoApimachineryPkgApisMetaV1APIResourceList v1get_api_sub_resources()



Get a KubeVirt API resources

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_response = api_instance.v1get_api_sub_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1get_api_sub_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**K8sIoApimachineryPkgApisMetaV1APIResourceList**](K8sIoApimachineryPkgApisMetaV1APIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1start_cluster_profiler**
> v1start_cluster_profiler()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1start_cluster_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->v1start_cluster_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1stop_cluster_profiler**
> v1stop_cluster_profiler()



### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()

try: 
    api_instance.v1stop_cluster_profiler()
except ApiException as e:
    print("Exception when calling DefaultApi->v1stop_cluster_profiler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1usbredir**
> v1usbredir(name, namespace)



Open a websocket connection to connect to USB device on the specified VirtualMachineInstance.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_instance.v1usbredir(name, namespace)
except ApiException as e:
    print("Exception when calling DefaultApi->v1usbredir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vm_addvolume**
> str v1vm_addvolume(name, namespace, body)



Add a volume and disk to a running Virtual Machine.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1AddVolumeOptions() # V1AddVolumeOptions | 

try: 
    api_response = api_instance.v1vm_addvolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vm_addvolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1AddVolumeOptions**](V1AddVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vm_expand_spec**
> str v1vm_expand_spec(name, namespace)



Get VirtualMachine object with expanded instancetype and preference.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects

try: 
    api_response = api_instance.v1vm_expand_spec(name, namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vm_expand_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vm_port_forward**
> v1vm_port_forward(name, namespace, port)



Open a websocket connection forwarding traffic to the running VMI for the specified VirtualMachine and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1vm_port_forward(name, namespace, port)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vm_port_forward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vm_port_forward_with_protocol**
> v1vm_port_forward_with_protocol(name, namespace, port, protocol)



Open a websocket connection forwarding traffic of the specified protocol (either tcp or udp) to the specified VirtualMachine and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.
protocol = 'protocol_example' # str | The protocol for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1vm_port_forward_with_protocol(name, namespace, port, protocol)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vm_port_forward_with_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 
 **protocol** | **str**| The protocol for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vm_removevolume**
> str v1vm_removevolume(name, namespace, body)



Removes a volume and disk from a running Virtual Machine.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1RemoveVolumeOptions() # V1RemoveVolumeOptions | 

try: 
    api_response = api_instance.v1vm_removevolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vm_removevolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1RemoveVolumeOptions**](V1RemoveVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vmi_addvolume**
> str v1vmi_addvolume(name, namespace, body)



Add a volume and disk to a running Virtual Machine Instance

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1AddVolumeOptions() # V1AddVolumeOptions | 

try: 
    api_response = api_instance.v1vmi_addvolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vmi_addvolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1AddVolumeOptions**](V1AddVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vmi_port_forward**
> v1vmi_port_forward(name, namespace, port)



Open a websocket connection forwarding traffic to the specified VirtualMachineInstance and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1vmi_port_forward(name, namespace, port)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vmi_port_forward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vmi_port_forward_with_protocol**
> v1vmi_port_forward_with_protocol(name, namespace, port, protocol)



Open a websocket connection forwarding traffic of the specified protocol (either tcp or udp) to the specified VirtualMachineInstance and port.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
port = 'port_example' # str | The target port for portforward on the VirtualMachineInstance.
protocol = 'protocol_example' # str | The protocol for portforward on the VirtualMachineInstance.

try: 
    api_instance.v1vmi_port_forward_with_protocol(name, namespace, port, protocol)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vmi_port_forward_with_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **port** | **str**| The target port for portforward on the VirtualMachineInstance. | 
 **protocol** | **str**| The protocol for portforward on the VirtualMachineInstance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1vmi_removevolume**
> str v1vmi_removevolume(name, namespace, body)



Removes a volume and disk from a running Virtual Machine Instance

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
name = 'name_example' # str | Name of the resource
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
body = kubevirt.V1RemoveVolumeOptions() # V1RemoveVolumeOptions | 

try: 
    api_response = api_instance.v1vmi_removevolume(name, namespace, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->v1vmi_removevolume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the resource | 
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **body** | [**V1RemoveVolumeOptions**](V1RemoveVolumeOptions.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_kube_virt_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_kube_virt_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a KubeVirtList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_kube_virt_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_kube_virt_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_migration_policy_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_migration_policy_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a MigrationPolicyList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_migration_policy_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_migration_policy_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_kube_virt**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_kube_virt(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a KubeVirt object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_kube_virt(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_kube_virt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachine object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_export**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_export(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineExport object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_export(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_instance**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_instance(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstance object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_instance(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_instance_migration**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_instance_migration(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstanceMigration object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_instance_migration(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_instance_migration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_instance_preset**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_instance_preset(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstancePreset object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_instance_preset(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_instance_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_instance_replica_set**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_instance_replica_set(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstanceReplicaSet object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_instance_replica_set(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_instance_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_instancetype**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_instancetype(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstancetype object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_instancetype(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_instancetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_pool**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_pool(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachinePool object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_pool(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_preference**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_preference(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachinePreference object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_preference(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_restore**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_restore(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineRestore object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_restore(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_snapshot**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_snapshot(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineSnapshot object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_snapshot(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_virtual_machine_snapshot_content**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_namespaced_virtual_machine_snapshot_content(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineSnapshotContent object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
namespace = 'namespace_example' # str | Object name and auth scope, such as for teams and projects
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_virtual_machine_snapshot_content(namespace, _continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_namespaced_virtual_machine_snapshot_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| Object name and auth scope, such as for teams and projects | 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_clone_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_clone_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineCloneList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_clone_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_clone_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_cluster_instancetype_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_cluster_instancetype_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineClusterInstancetypeList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_cluster_instancetype_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_cluster_instancetype_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_cluster_preference_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_cluster_preference_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineClusterPreferenceList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_cluster_preference_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_cluster_preference_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_export_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_export_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineExportList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_export_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_export_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_instance_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_instance_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstanceList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_instance_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_instance_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_instance_migration_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_instance_migration_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstanceMigrationList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_instance_migration_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_instance_migration_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_instance_preset_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_instance_preset_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstancePresetList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_instance_preset_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_instance_preset_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_instance_replica_set_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_instance_replica_set_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstanceReplicaSetList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_instance_replica_set_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_instance_replica_set_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_instancetype_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_instancetype_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineInstancetypeList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_instancetype_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_instancetype_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_pool_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_pool_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachinePoolList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_pool_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_pool_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_preference_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_preference_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachinePreferenceList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_preference_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_preference_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_restore_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_restore_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineRestoreList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_restore_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_restore_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_snapshot_content_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_snapshot_content_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineSnapshotContentList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_snapshot_content_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_snapshot_content_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_virtual_machine_snapshot_list_for_all_namespaces**
> K8sIoApimachineryPkgApisMetaV1WatchEvent watch_virtual_machine_snapshot_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



Watch a VirtualMachineSnapshotList object.

### Example 
```python
from __future__ import print_function
import time
import kubevirt
from kubevirt.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubevirt.DefaultApi()
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | TimeoutSeconds for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_virtual_machine_snapshot_list_for_all_namespaces(_continue=_continue, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->watch_virtual_machine_snapshot_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server the server will respond with a 410 ResourceExpired error indicating the client must restart their list without the continue field. This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| TimeoutSeconds for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**K8sIoApimachineryPkgApisMetaV1WatchEvent**](K8sIoApimachineryPkgApisMetaV1WatchEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

