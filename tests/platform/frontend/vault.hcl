storage "consul" {
  address       = "cube:8500"
  path          = "vault"
  token		= "very-secret-token"
}

listener "tcp" {
  address       = "127.0.0.1:8200"
  tls_disable   = 1
  token         = "very-secret-token"
}
