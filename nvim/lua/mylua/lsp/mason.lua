local servers = {
    "lua_ls",
    "pyright",
    "clangd"
}

local settings = {
    ui = {
        border = "none",
        icons = {
            package_installed = "✓",
            package_pending = "➜",
            package_uninstalled = "✗"
        }
    },
    log_level = vim.log.levels.INFO,
    max_concurrent_installers = 4,
}

require("mason").setup(settings)
require("mason-lspconfig").setup({
    ensure_installed = servers,
    automatic_installation = true,
})

local lspconfig_status_ok, lspconfig = pcall(require, "lspconfig")
if not lspconfig_status_ok then
    print("Can not load lspconfig...")
    return
end

local opts = {}

for _, server in pairs(servers) do
    opts = {
        on_attach = require("mylua.lsp.handlers").on_attach,
        capabilities = require("mylua.lsp.handlers").capabilities,
    }

    server = vim.split(server, "@")[1]

    -- extend different lsp to further configuration...
    -- skip for now
--    local require_ok, conf_opts = pcall(require, )
    lspconfig[server].setup(opts)
end
