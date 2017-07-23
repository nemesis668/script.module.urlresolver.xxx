# script.module.urlresolver.xxx
Adult Resolver Extension for SMU

1. Import SMU and the XXX SMU Extension to your addon.
2. Load the script.module.urlresolver.xxx plugins directory from within your addon.

    import urlresolver, os, xbmcaddon
    
    smu_xxx_path = xbmcaddon.Addon("script.module.urlresolver.xxx").getAddonInfo("path")
    
    smu_xxx_dir = os.path.join(smu_xxx_path,'resources/plugins/')
    
    urlresolver.add_plugin_dirs(smu_xxx_dir)
    
3. Call the urlresolver as normal to resolve the XXX hosts.
