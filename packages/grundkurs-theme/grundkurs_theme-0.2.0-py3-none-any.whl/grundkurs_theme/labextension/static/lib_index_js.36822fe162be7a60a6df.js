"use strict";
(self["webpackChunkgrundkurs_theme"] = self["webpackChunkgrundkurs_theme"] || []).push([["lib_index_js"],{

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "requestAPI": () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'grundkurs_theme', endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    const data = await response.json();
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ContentFactoryWithFooterButton": () => (/* binding */ ContentFactoryWithFooterButton),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/codeeditor */ "webpack/sharing/consume/default/@jupyterlab/codeeditor");
/* harmony import */ var _jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");






const PLUGIN_ID = 'grundkurs_theme:plugin';
/**
 * Initialization data for the grundkurs_theme extension.
 */
const plugin = {
    id: PLUGIN_ID,
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.IThemeManager, _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__.ISettingRegistry],
    activate: (app, tracker, manager, settings) => {
        const { commands, shell } = app;
        const command = 'grundkurs:send-feedback';
        let url = '';
        /**
         * Load the settings for this extension
         *
         * @param setting Extension settings
         */
        function loadSetting(setting) {
            // Read the settings and convert to the correct type
            url = setting.get('url').composite;
        }
        // Wait for the application to be restored and
        // for the settings for this plugin to be loaded
        Promise.all([app.restored, settings.load(PLUGIN_ID)])
            .then(([, setting]) => {
            // Read the settings
            loadSetting(setting);
            // Listen for your plugin setting changes using Signal
            setting.changed.connect(loadSetting);
            commands.addCommand(command, {
                label: 'Send feedback for this assignment',
                execute: async (args) => {
                    var _a, _b;
                    const current = getCurrent(tracker, shell, args);
                    if (current) {
                        // Get cellid of current active cell
                        const cellId = (_b = (_a = current.content.activeCell) === null || _a === void 0 ? void 0 : _a.model) === null || _b === void 0 ? void 0 : _b.modelDB.basePath;
                        const value = args['value'];
                        // POST request
                        const dataToSend = { 'cellId': cellId, url, value };
                        try {
                            console.log(JSON.stringify(dataToSend));
                            const reply = await (0,_handler__WEBPACK_IMPORTED_MODULE_4__.requestAPI)('feedback', {
                                body: JSON.stringify(dataToSend),
                                method: 'POST',
                            });
                            console.log(reply);
                        }
                        catch (reason) {
                            console.error(`Error on POST /feedback ${dataToSend}.\n${reason}`);
                        }
                    }
                },
            });
        });
        console.log('JupyterLab extension grundkurs_theme is activated!');
        const style = 'grundkurs_theme/index.css';
        manager.register({
            name: 'grundkurs_theme',
            isLight: true,
            load: () => manager.loadCSS(style),
            unload: () => Promise.resolve(undefined)
        });
    }
};
// Get the current widget and activate unless the args specify otherwise.
function getCurrent(tracker, shell, args) {
    const widget = tracker.currentWidget;
    const activate = args['activate'] !== false;
    if (activate && widget) {
        shell.activateById(widget.id);
    }
    return widget;
}
/**
 * Extend the default implementation of an `IContentFactory`.
 */
class ContentFactoryWithFooterButton extends _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookPanel.ContentFactory {
    constructor(commands, options) {
        super(options);
        this.commands = commands;
    }
    /**
     * Create a new cell header for the parent widget.
     */
    createCellFooter() {
        return new _widget__WEBPACK_IMPORTED_MODULE_5__.CellFooterWithButton(this.commands);
    }
    createMarkdownCell(options, parent) {
        var _a, _b, _c;
        //const cellId = options.model?.modelDB.basePath
        console.log(options);
        console.log((_a = options.model) === null || _a === void 0 ? void 0 : _a.value.text);
        console.log(parent);
        console.log((_b = parent.model) === null || _b === void 0 ? void 0 : _b.cells);
        const existingCell = options.model;
        if (existingCell) {
            const content = existingCell.value.text + 'New content';
            existingCell.value.text = content;
        }
        if ((_c = parent.model) === null || _c === void 0 ? void 0 : _c.cells) {
            console.log('been here');
            for (let i = 0; i < parent.model.cells.length; i++) {
                const cell = parent.model.cells.get(i);
                console.log(cell);
                //if (cell.type === 'markdown' && cell.metadata.get('path') === basePath) {
                //  break;
                //}
            }
        }
        return super.createMarkdownCell(options, parent);
    }
}
/**
 * The notebook cell factory provider.
 */
const cellFactory = {
    id: 'jupyterlab-cellcodebtn:factory',
    provides: _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookPanel.IContentFactory,
    requires: [_jupyterlab_codeeditor__WEBPACK_IMPORTED_MODULE_3__.IEditorServices],
    autoStart: true,
    activate: (app, editorServices) => {
        // tslint:disable-next-line:no-console
        console.log('JupyterLab extension jupyterlab-cellcodebtn', 'overrides default nootbook content factory');
        const { commands } = app;
        const editorFactory = editorServices.factoryService.newInlineEditor;
        return new ContentFactoryWithFooterButton(commands, { editorFactory });
    }
};
/**
 * Export this plugins as default.
 */
const plugins = [
    plugin,
    cellFactory
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CellFooterWithButton": () => (/* binding */ CellFooterWithButton),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);


const StarRating = ({ submit }) => {
    const [rating, setRating] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(0);
    const [clicked, setClicked] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    const [submitted, setSubmitted] = (0,react__WEBPACK_IMPORTED_MODULE_1__.useState)(false);
    (0,react__WEBPACK_IMPORTED_MODULE_1__.useEffect)(() => {
        if (submitted) {
            setTimeout(() => {
                setSubmitted(false);
            }, 5000);
        }
    }, [submitted]);
    // @ts-ignore
    const handleClick = (index) => {
        setRating(index + 1);
        setClicked(true);
    };
    // @ts-ignore
    const handleSubmit = async () => {
        // logic to handle the submit event goes here
        console.log(`Rating submitted: ${rating}`);
        setClicked(false);
        submit(rating).then(() => setSubmitted(true)).catch(e => console.log(e));
    };
    const ratings = [
        "too easy",
        "easy",
        "good",
        "hard",
        "too hard"
    ];
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: CELL_FOOTER_DIV_CLASS },
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", { className: "exercise_label" }, "Feedback"),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: 'star-rating' }, ['😜', '😛', '🙂', '😕', '😖'].map((star, index) => (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", { onClick: () => handleClick(index), style: { margin: '10px' } }, star)))),
        clicked && (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { style: { display: 'flex', flexDirection: 'column', width: '280px', justifyContent: 'space-around' } },
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: "submitted-message" },
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("b", null, "You:"),
                " ",
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null,
                    "The exercise was ",
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("b", null, ratings[rating - 1])),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("button", { className: "submit-button", onClick: () => handleSubmit() }, "Submit")))),
        submitted && (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: "submitted-message" },
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement("b", null, "Us:"),
            " Thank you for submitting your feedback \uD83D\uDE4F"))));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (StarRating);
/**
 * The CSS classes added to the cell footer.
 */
const CELL_FOOTER_DIV_CLASS = 'gk-cellFeedbackContainer';
//const CELL_FOOTER_BUTTON_CLASS = 'gk-cellFeedbackBtn';
/**
 * Extend default implementation of a cell footer.
 */
class CellFooterWithButton extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    /**
     * Construct a new cell footer.
     */
    constructor(commands) {
        super();
        this.commands = commands;
    }
    render() {
        var _a;
        const metadata = this.parent.model.sharedModel.getMetadata();
        return (
        // TOOD: check for specific tag
        ((_a = metadata.tags) === null || _a === void 0 ? void 0 : _a.includes("exercise")) ?
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement(StarRating, { submit: (i) => {
                    // We return the Promise, so that the component can react on completion 
                    return this.commands.execute('grundkurs:send-feedback', { value: i });
                } })
            // Return empty tag
            : react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null));
    }
}


/***/ })

}]);
//# sourceMappingURL=lib_index_js.36822fe162be7a60a6df.js.map