resource "mongodbatlas_project" "horus-project-prod" {
  org_id = mongodbatlas_organization.horus.id
  name   = "Pylegends"
}