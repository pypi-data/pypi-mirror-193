// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module collaboration-extension
 */
import { defaultFileBrowser } from './filebrowser';
import { userMenuPlugin, menuBarPlugin, rtcGlobalAwarenessPlugin, rtcPanelPlugin } from './collaboration';
/**
 * Export the plugins as default.
 */
const plugins = [
    defaultFileBrowser,
    userMenuPlugin,
    menuBarPlugin,
    rtcGlobalAwarenessPlugin,
    rtcPanelPlugin
];
export default plugins;
