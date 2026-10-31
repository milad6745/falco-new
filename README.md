# Falco offline starter — Kubernetes v1.25.6 / Ubuntu 24.04 / kernel 6.14.0-32-generic

## This is a starter, not a verified installation bundle

The included GitHub Actions workflow fetches a **pinned Falco Helm chart**, renders it with kmod settings, downloads all images referenced in the render (amd64), and bundles Falco source corresponding to the chart appVersion. **It does NOT build or include `falco.ko`**, and offline installation is not yet safe until a kmod build and load test succeeds on a test node.

### Run
1. Create a GitHub repository; upload the contents of this directory including `.github/workflows/build.yml`.
2. Open **Actions > Build Falco offline assets > Run workflow**; retain the default chart version `6.0.2` initially.
3. After the job finishes, download the `falco-offline-assets` artifact and extract the `.tar.gz` inside it.
4. Check `charts/`, `images/`, `drivers/falco-source.tar.gz`, `values/`, and `manifests/`.

### Important limitations
- Chart v6.0.2 is a **starting pinned choice** and its Kubernetes v1.25.6 compatibility still needs validation against rendered manifests and a test cluster.
- Because the worker uses Ubuntu `6.14.0-32-generic`, the `falco.ko` kernel module must be built/tested against the **exact matching** headers `6.14.0-32.32~24.04.1`. Do not install a module compiled for a different kernel. The relevant GCC is 13.3.0.
- The driver loader may try network access unless it is configured to use an offline prebuilt driver or an offline build path. Disable all external network access in the final environment and validate the actual generated manifests.
- If Secure Boot enforces signatures, a custom kernel module may require trusted signing. `mokutil` was absent on the worker, so the Secure Boot state is not confirmed.
- When retagging images for Nexus, adjust chart values for both Falco and driver-loader and re-render the chart before deployment. The images archives retain original names for portability.
- If an older Falco is already running, avoid installing a second agent on the same node until driver conflicts and duplication have been evaluated.

Official references:
https://falco.org/docs/setup/kubernetes/
https://falco.org/docs/setup/tarball/
https://falco.org/docs/developer-guide/source/
