resource "mongodbatlas_organization" "horus" {
  name        = "Horus"
  description = "Software House"
  org_owner_id = var.org_owner_id
  role_names = ["ORG_OWNER"]
}