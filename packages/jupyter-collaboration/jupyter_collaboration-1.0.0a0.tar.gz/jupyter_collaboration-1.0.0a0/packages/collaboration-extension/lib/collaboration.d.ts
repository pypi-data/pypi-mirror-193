/**
 * @packageDocumentation
 * @module collaboration-extension
 */
import { JupyterFrontEndPlugin } from '@jupyterlab/application';
import { IAwareness, IUserMenu } from '@jupyter/collaboration';
/**
 * Jupyter plugin providing the IUserMenu.
 */
export declare const userMenuPlugin: JupyterFrontEndPlugin<IUserMenu>;
/**
 * Jupyter plugin adding the IUserMenu to the menu bar if collaborative flag enabled.
 */
export declare const menuBarPlugin: JupyterFrontEndPlugin<void>;
/**
 * Jupyter plugin creating a global awareness for RTC.
 */
export declare const rtcGlobalAwarenessPlugin: JupyterFrontEndPlugin<IAwareness>;
/**
 * Jupyter plugin adding the RTC information to the application left panel if collaborative flag enabled.
 */
export declare const rtcPanelPlugin: JupyterFrontEndPlugin<void>;
