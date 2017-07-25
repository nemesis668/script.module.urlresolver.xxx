# script.module.urlresolver.xxx
Adult Resolver Extension for SMU

1. Import SMU >= 3.0.37 and the XXX SMU Extension to your addon.
2. Call the urlresolver from your addon to resolve the XXX hosts.

    * from urlresolver.hmf import HostedMediaFile
    * url = HostedMediaFile(url=url, include_xxx=True).resolve()
    
    or
    
    * import urlresolver
    * url = urlresolver.resolve(url, include_xxx=True)
