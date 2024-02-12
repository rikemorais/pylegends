resource "mongodbatlas_cluster" "pylegends" {
  project_id              = mongodbatlas_project.horus-project-prod.id
  name                    = "pylegends"
  provider_name           = "TERRAFORM"
  cluster_type            = "REPLICASET"
  disk_size_gb            = 10
  num_shards              = 1
  replication_factor      = 3
  auto_scaling_disk_gb_enabled = false
  provider_instance_size_name   = "M10"
}