import { User } from '@jupyterlab/services';
import { DocumentChange, YDocument } from '@jupyter/ydoc';
import { IDisposable } from '@lumino/disposable';
/**
 * An interface for a document provider.
 */
export interface IDocumentProvider extends IDisposable {
    /**
     * Returns a Promise that resolves when the document provider is ready.
     */
    readonly ready: Promise<void>;
}
/**
 * A class to provide Yjs synchronization over WebSocket.
 *
 * We specify custom messages that the server can interpret. For reference please look in yjs_ws_server.
 *
 */
export declare class WebSocketProvider implements IDocumentProvider {
    /**
     * Construct a new WebSocketProvider
     *
     * @param options The instantiation options for a WebSocketProvider
     */
    constructor(options: WebSocketProvider.IOptions);
    /**
     * Test whether the object has been disposed.
     */
    get isDisposed(): boolean;
    /**
     * A promise that resolves when the document provider is ready.
     */
    get ready(): Promise<void>;
    /**
     * Dispose of the resources held by the object.
     */
    dispose(): void;
    private _onUserChanged;
    private _awareness;
    private _contentType;
    private _format;
    private _isDisposed;
    private _path;
    private _ready;
    private _serverUrl;
    private _ydoc;
    private _yWebsocketProvider;
}
/**
 * A namespace for WebSocketProvider statics.
 */
export declare namespace WebSocketProvider {
    /**
     * The instantiation options for a WebSocketProvider.
     */
    interface IOptions {
        /**
         * The server URL
         */
        url: string;
        /**
         * The document file path
         */
        path: string;
        /**
         * Content type
         */
        contentType: string;
        /**
         * The source format
         */
        format: string;
        /**
         * The shared model
         */
        model: YDocument<DocumentChange>;
        /**
         * The user data
         */
        user: User.IManager;
    }
}
