/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
import { URLExt } from '@jupyterlab/coreutils';
import { ServerConnection } from '@jupyterlab/services';
import { PromiseDelegate } from '@lumino/coreutils';
import { Signal } from '@lumino/signaling';
import { WebsocketProvider as YWebsocketProvider } from 'y-websocket';
/**
 * Room Id endpoint provided by `jupyter_collaboration`
 * See https://github.com/jupyterlab/jupyter_collaboration
 */
const FILE_PATH_TO_ROOM_ID_URL = 'api/yjs/roomid';
/**
 * A class to provide Yjs synchronization over WebSocket.
 *
 * We specify custom messages that the server can interpret. For reference please look in yjs_ws_server.
 *
 */
export class WebSocketProvider {
    /**
     * Construct a new WebSocketProvider
     *
     * @param options The instantiation options for a WebSocketProvider
     */
    constructor(options) {
        this._ready = new PromiseDelegate();
        this._isDisposed = false;
        this._path = options.path;
        this._contentType = options.contentType;
        this._format = options.format;
        this._serverUrl = options.url;
        this._ydoc = options.model.ydoc;
        this._awareness = options.model.awareness;
        this._yWebsocketProvider = null;
        const user = options.user;
        user.ready
            .then(() => {
            this._onUserChanged(user);
        })
            .catch(e => console.error(e));
        user.userChanged.connect(this._onUserChanged, this);
        const serverSettings = ServerConnection.makeSettings();
        const url = URLExt.join(serverSettings.baseUrl, FILE_PATH_TO_ROOM_ID_URL, encodeURIComponent(this._path));
        const data = {
            method: 'PUT',
            body: JSON.stringify({ format: this._format, type: this._contentType })
        };
        ServerConnection.makeRequest(url, data, serverSettings)
            .then(response => {
            if (response.status !== 200 && response.status !== 201) {
                throw new ServerConnection.ResponseError(response);
            }
            return response.text();
        })
            .then(roomid => {
            this._yWebsocketProvider = new YWebsocketProvider(this._serverUrl, roomid, this._ydoc, {
                awareness: this._awareness
            });
        })
            .then(() => this._ready.resolve())
            .catch(reason => console.warn(reason));
    }
    /**
     * Test whether the object has been disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    /**
     * A promise that resolves when the document provider is ready.
     */
    get ready() {
        return this._ready.promise;
    }
    /**
     * Dispose of the resources held by the object.
     */
    dispose() {
        var _a;
        if (this.isDisposed) {
            return;
        }
        this._isDisposed = true;
        (_a = this._yWebsocketProvider) === null || _a === void 0 ? void 0 : _a.destroy();
        Signal.clearData(this);
    }
    _onUserChanged(user) {
        this._awareness.setLocalStateField('user', user.identity);
    }
}
