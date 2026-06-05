const launcher = {
    blockTargetDevices: true,
    launch: function(titleId) {
        if (this.blockTargetDevices && this.isRestrictedDevice()) {
            return;
        }
        const uri = `pspkmvc:?category=gp&titleid=${titleId}`;
        try {
            window.location.href = uri;
        } catch (err) {
            console.error("fuckkkkkk");
        }
    },
    isRestrictedDevice: function() {
        const ua = navigator.userAgent;
        return /PlayStation Vita/i.test(ua);
    }
};
// launcher.launch("NPXS10007");
