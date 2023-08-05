import typing as t
from time import sleep
from traceback import format_exception
from typing import cast

from lk_utils import new_thread
from lk_utils import xpath
from lk_utils.subproc import ThreadWorker

from qmlease import AutoProp
from qmlease import QObject
from qmlease import app
from qmlease import bind_signal
from qmlease import pyassets
from qmlease import signal
from qmlease import slot


def launch_app() -> None:
    pyassets.set_root(xpath('qml/Assets'))
    app.set_app_icon(xpath('../launcher.ico'))
    app.register(Home())
    app.run(xpath('qml/Home.qml'))
    # app.run(xpath('qml/Home.qml'), debug=True)


class Home(QObject):
    running = cast(bool, AutoProp(False))
    _info_item: QObject
    _info_updated = signal(str)  # this is for sub-thread to emit.
    _installation_done = signal(bool)
    _installing_thread: t.Optional[ThreadWorker] = None
    
    @slot(result=str)
    def get_app_version(self) -> str:
        from ... import __version__
        return f'v{__version__}'
    
    @slot(object, object, object, object)
    def init_view(
            self,
            input_bar: QObject,
            install_btn: QObject,
            stop_btn: QObject,
            info: QObject
    ) -> None:
        self._info_item = info
        self._info_item['text'] = _default_text = _gray(
            'Input an appid to install. '
            'For example: "hello_world".'
        )
        
        @bind_signal(input_bar.submit)
        def _(text: str) -> None:
            self._install(text)
        
        @bind_signal(self._info_updated)
        def _(text: str) -> None:
            self._info_item['text'] = text
        
        @bind_signal(self.running_changed)
        def _(running: bool) -> None:
            install_btn['text'] = 'Install' if not running else 'Installing...'
            stop_btn['width'] = 100 if running else 0
        
        @bind_signal(install_btn.clicked)
        def _() -> None:
            self._install(input_bar['text'])
        
        @bind_signal(self._installation_done)
        def _(success: bool) -> None:
            # self._installing_thread.join()
            self._stop_timer()
            if success:
                self._transient_info(
                    _green('Installation done.'),
                    _default_text
                )
            else:
                self._transient_info(
                    _red('Installation failed. '
                         'See console output for details.'),
                    _default_text,
                    duration=5
                )
        
        @bind_signal(stop_btn.clicked)
        def _() -> None:
            if self._installing_thread.kill():
                self._stop_timer()
                self._transient_info(
                    _red('User force stopped.'),
                    _default_text
                )
            else:
                self._transient_info(
                    _red('Failed to stop the task! If you want to manually '
                         'stop it, please shutdown the window and restart it.'),
                    duration=10
                )
    
    def _install(self, appid: str) -> None:
        # check ability
        if self.running:
            self._transient_info(_yellow('Task is already running!'))
            return
        if not appid:
            self._transient_info(_red('Appid cannot be empty!'))
            return
        
        @new_thread()
        def install(appid: str) -> None:
            from ...__main__ import install
            try:
                install(appid)
                self._installation_done.emit(True)
            except Exception as e:
                print(''.join(format_exception(e)), ':v4')
                self._installation_done.emit(False)
        
        self._start_timer(appid)
        install(appid)
    
    @new_thread()
    def _start_timer(self, appid: str) -> None:
        time_sec = 0
        self.running = True
        while True:
            sleep(1)
            time_sec += 1
            if self.running:
                self._info_updated.emit(
                    f'Installing {appid}... (time elapsed: {time_sec}s)'
                )
            else:
                break
    
    def _stop_timer(self) -> None:
        self.running = False
    
    @new_thread()
    def _transient_info(
            self,
            text: str,
            restore: str = None,
            duration: float = 3.0
    ) -> None:
        """
        do not set text directly, because sub thread cannot do this. use signal
        to emit info change.
        """
        if restore is None:
            restore = self._info_item['text']
        self._info_updated.emit(text)
        sleep(duration)
        self._info_updated.emit(restore)


def _gray(text: str) -> str:
    return f'<font color="gray">{text}</font>'


def _red(text: str) -> str:
    return f'<font color="red">{text}</font>'


def _green(text: str) -> str:
    return f'<font color="green">{text}</font>'


def _yellow(text: str) -> str:
    return f'<font color="yellow">{text}</font>'
