// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module collaboration-extension
 */
import { PageConfig } from '@jupyterlab/coreutils';
import { DOMUtils } from '@jupyterlab/apputils';
import { AwarenessMock, CollaboratorsPanel, IGlobalAwareness, IUserMenu, RendererUserMenu, UserInfoPanel, UserMenu } from '@jupyter/collaboration';
import { SidePanel, usersIcon } from '@jupyterlab/ui-components';
import { MenuBar } from '@lumino/widgets';
import { URLExt } from '@jupyterlab/coreutils';
import { ServerConnection } from '@jupyterlab/services';
import { IStateDB } from '@jupyterlab/statedb';
import { ITranslator } from '@jupyterlab/translation';
import * as Y from 'yjs';
import { Awareness } from 'y-protocols/awareness';
import { WebsocketProvider } from 'y-websocket';
/**
 * Jupyter plugin providing the IUserMenu.
 */
export const userMenuPlugin = {
    id: '@jupyter/collaboration-extension:userMenu',
    autoStart: true,
    requires: [],
    provides: IUserMenu,
    activate: (app) => {
        const { commands } = app;
        const { user } = app.serviceManager;
        return new UserMenu({ commands, user });
    }
};
/**
 * Jupyter plugin adding the IUserMenu to the menu bar if collaborative flag enabled.
 */
export const menuBarPlugin = {
    id: '@jupyter/collaboration-extension:userMenuBar',
    autoStart: true,
    requires: [IUserMenu],
    activate: async (app, menu) => {
        const { shell } = app;
        const { user } = app.serviceManager;
        if (PageConfig.getOption('collaborative') !== 'true') {
            return;
        }
        const menuBar = new MenuBar({
            forceItemsPosition: {
                forceX: false,
                forceY: false
            },
            renderer: new RendererUserMenu(user)
        });
        menuBar.id = 'jp-UserMenu';
        user.userChanged.connect(() => menuBar.update());
        menuBar.addMenu(menu);
        shell.add(menuBar, 'top', { rank: 1000 });
    }
};
/**
 * Jupyter plugin creating a global awareness for RTC.
 */
export const rtcGlobalAwarenessPlugin = {
    id: '@jupyter/collaboration-extension:rtcGlobalAwareness',
    autoStart: true,
    requires: [IStateDB],
    provides: IGlobalAwareness,
    activate: (app, state) => {
        const { user } = app.serviceManager;
        const ydoc = new Y.Doc();
        if (PageConfig.getOption('collaborative') !== 'true') {
            return new AwarenessMock(ydoc);
        }
        const awareness = new Awareness(ydoc);
        const server = ServerConnection.makeSettings();
        const url = URLExt.join(server.wsUrl, 'api/yjs');
        new WebsocketProvider(url, 'JupyterLab:globalAwareness', ydoc, {
            awareness: awareness
        });
        const userChanged = () => {
            awareness.setLocalStateField('user', user.identity);
        };
        if (user.isReady) {
            userChanged();
        }
        user.ready.then(userChanged).catch(e => console.error(e));
        user.userChanged.connect(userChanged);
        state.changed.connect(async () => {
            var _a, _b;
            const data = await state.toJSON();
            const current = ((_b = (_a = data['layout-restorer:data']) === null || _a === void 0 ? void 0 : _a.main) === null || _b === void 0 ? void 0 : _b.current) || '';
            if (current.startsWith('editor') || current.startsWith('notebook')) {
                awareness.setLocalStateField('current', current);
            }
            else {
                awareness.setLocalStateField('current', null);
            }
        });
        return awareness;
    }
};
/**
 * Jupyter plugin adding the RTC information to the application left panel if collaborative flag enabled.
 */
export const rtcPanelPlugin = {
    id: '@jupyter/collaboration-extension:rtcPanel',
    autoStart: true,
    requires: [IGlobalAwareness, ITranslator],
    activate: (app, awareness, translator) => {
        if (PageConfig.getOption('collaborative') !== 'true') {
            return;
        }
        const { user } = app.serviceManager;
        const trans = translator.load('jupyterlab');
        const userPanel = new SidePanel();
        userPanel.id = DOMUtils.createDomID();
        userPanel.title.icon = usersIcon;
        userPanel.title.caption = trans.__('Collaboration');
        userPanel.addClass('jp-RTCPanel');
        app.shell.add(userPanel, 'left', { rank: 300 });
        const currentUserPanel = new UserInfoPanel(user);
        currentUserPanel.title.label = trans.__('User info');
        currentUserPanel.title.caption = trans.__('User information');
        userPanel.addWidget(currentUserPanel);
        const fileopener = (path) => {
            void app.commands.execute('docmanager:open', { path });
        };
        const collaboratorsPanel = new CollaboratorsPanel(user, awareness, fileopener);
        collaboratorsPanel.title.label = trans.__('Online Collaborators');
        userPanel.addWidget(collaboratorsPanel);
    }
};
