import { ILabShell, IRouter, JupyterFrontEnd } from '@jupyterlab/application';
import { IDefaultFileBrowser, IFileBrowserFactory } from '@jupyterlab/filebrowser';
import { YDrive } from '@jupyter/docprovider';
/**
 * The command IDs used by the file browser plugin.
 */
var CommandIDs;
(function (CommandIDs) {
    CommandIDs.openPath = 'filebrowser:open-path';
})(CommandIDs || (CommandIDs = {}));
/**
 * The default file browser factory provider.
 */
export const defaultFileBrowser = {
    id: '@jupyter/collaboration-extension:defaultFileBrowser',
    provides: IDefaultFileBrowser,
    requires: [IFileBrowserFactory],
    optional: [IRouter, JupyterFrontEnd.ITreeResolver, ILabShell],
    activate: async (app, fileBrowserFactory, router, tree, labShell) => {
        console.debug('@jupyter/collaboration-extension:defaultFileBrowser: activated');
        const { commands } = app;
        const drive = new YDrive(app.serviceManager.user);
        app.serviceManager.contents.addDrive(drive);
        // Manually restore and load the default file browser.
        const defaultBrowser = fileBrowserFactory.createFileBrowser('filebrowser', {
            auto: false,
            restore: false,
            driveName: 'YDrive'
        });
        void Private.restoreBrowser(defaultBrowser, commands, router, tree, labShell);
        return defaultBrowser;
    }
};
var Private;
(function (Private) {
    /**
     * Restores file browser state and overrides state if tree resolver resolves.
     */
    async function restoreBrowser(browser, commands, router, tree, labShell) {
        const restoring = 'jp-mod-restoring';
        browser.addClass(restoring);
        if (!router) {
            await browser.model.restore(browser.id);
            await browser.model.refresh();
            browser.removeClass(restoring);
            return;
        }
        const listener = async () => {
            router.routed.disconnect(listener);
            const paths = await (tree === null || tree === void 0 ? void 0 : tree.paths);
            if ((paths === null || paths === void 0 ? void 0 : paths.file) || (paths === null || paths === void 0 ? void 0 : paths.browser)) {
                // Restore the model without populating it.
                await browser.model.restore(browser.id, false);
                if (paths.file) {
                    await commands.execute(CommandIDs.openPath, {
                        path: paths.file,
                        dontShowBrowser: true
                    });
                }
                if (paths.browser) {
                    await commands.execute(CommandIDs.openPath, {
                        path: paths.browser,
                        dontShowBrowser: true
                    });
                }
            }
            else {
                await browser.model.restore(browser.id);
                await browser.model.refresh();
            }
            browser.removeClass(restoring);
            if (labShell === null || labShell === void 0 ? void 0 : labShell.isEmpty('main')) {
                void commands.execute('launcher:create');
            }
        };
        router.routed.connect(listener);
    }
    Private.restoreBrowser = restoreBrowser;
})(Private || (Private = {}));
