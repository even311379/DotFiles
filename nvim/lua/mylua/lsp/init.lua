local status_ok, _ = pcall(require, "lspconfig")
if not status_ok then
    print("can not load lspconfig")
    return
end

require "mylua.lsp.mason"
require("mylua.lsp.handlers").setup()
require "mylua.lsp.null-ls"

