# -*- coding: utf-8 -*-
# Phan mem cai loa cho may tinh (Windows/macOS): the tai ve tren trang Tai app + trang huong dan /<lang>/cai-loa/
# Chu cua cac buoc bat Go loi USB lay tu giao dien phan mem (cailoa_ui.json, sinh khi chup hinh) de web va phan mem luon khop.
import json, os
UI = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cailoa_ui.json'), encoding='utf-8'))
WIN = "/tai/windows"
MAC = "/tai/mac"
WIN_LATEST = "https://raw.githubusercontent.com/karaokeaihome/app/main/cai-loa/KaraokeAIHome-CaiLoa.exe"
MAC_LATEST = "https://raw.githubusercontent.com/karaokeaihome/app/main/cai-loa/KaraokeAIHome-CaiLoa-mac.zip"
T = {}
T['vi'] = dict(
 card_h="Phần mềm nâng cấp loa cho máy tính", card_p="Tự cài và cập nhật phần mềm Karaoke AI Home mới nhất cho loa qua Wi‑Fi, bằng máy tính Windows hoặc Mac. Luôn tải về bản mới nhất.",
 win="Tải cho Windows", mac="Tải cho macOS", guide="Xem hướng dẫn sử dụng",
 card_steps=["Tải phần mềm về máy tính và mở ra.","Trên loa, bật Gỡ lỗi USB một lần bằng điều khiển (có hình hướng dẫn).","Phần mềm tự tìm loa trong cùng mạng Wi‑Fi. Bấm <b>Cài đặt</b> và chờ báo <b>Xong</b>."],
 g_title="Hướng dẫn nâng cấp loa bằng máy tính",
 g_lead="Phần mềm nâng cấp loa giúp bạn tự nâng cấp loa lên phần mềm Karaoke AI Home mới nhất (giao diện 6 ngôn ngữ, trợ lý AI Lambo, ứng dụng) và cập nhật về sau, chỉ với một nút bấm.",
 need="Bạn cần: máy tính Windows 10/11 hoặc macOS 11 trở lên, có Internet, dùng chung mạng Wi‑Fi với loa, và điều khiển của loa.",
 h1="1. Tải và mở phần mềm",
 win_h="Windows", win_s=["Bấm <b>Tải cho Windows</b> để tải tệp <b>KaraokeAIHome-CaiLoa.exe</b>. Nếu trình duyệt hỏi, chọn <b>Giữ lại</b>.","Bấm đúp vào tệp vừa tải.","Nếu hiện <b>“Windows đã bảo vệ máy tính của bạn”</b>: bấm <b>Thông tin bổ sung</b> → <b>Vẫn chạy</b>.","Cửa sổ phần mềm nâng cấp loa mở ra."],
 mac_h="macOS", mac_s=["Bấm <b>Tải cho macOS</b>, mở tệp zip vừa tải để giải nén, được tệp <b>KaraokeAIHome-CaiLoa</b>.","Bấm đúp vào tệp đó.","Nếu macOS báo không mở được vì chưa xác minh: bấm <b>Xong</b>, vào <b>Cài đặt hệ thống → Quyền riêng tư & Bảo mật</b>, kéo xuống bấm <b>Vẫn mở</b>, rồi bấm <b>Mở</b>.","Một cửa sổ Terminal hiện ra (để nguyên trong khi cài) và cửa sổ phần mềm mở trong trình duyệt."],
 h2="2. Bật Gỡ lỗi USB trên loa (chỉ một lần)", h2_p="Bật loa, cho loa vào cùng mạng Wi‑Fi với máy tính, rồi làm theo hình bằng điều khiển. Chữ trên loa có thể là tiếng Trung, tiếng Anh hoặc tiếng Việt; vị trí các mục vẫn như hình.",
 h3="3. Cài đặt", s3=["Phần mềm tự tìm loa trong mạng. Loa hiện trong danh sách với chữ <b>Sẵn sàng</b>, bấm <b>Cài đặt</b>.","Phần mềm tải bản mới nhất từ máy chủ, chép vào loa và thiết lập. Thanh tiến độ cho biết đang làm bước nào.","Khi báo <b>Xong</b>, loa tự khởi động lại, khoảng 1 phút sau là dùng được."],
 h4="Cập nhật về sau", p4="Khi có bản mới, mở lại phần mềm: loa nào có bản mới sẽ hiện nút <b>Cập nhật</b>. Phần mềm luôn tải bản mới nhất từ máy chủ, nên không cần tải lại phần mềm trừ khi nó báo có bản phần mềm mới. Loa đã cài cũng có thể tự cập nhật bằng nút “Cập nhật phần mềm loa” trong app điện thoại.",
 h5="Không thấy loa?", h6="Lưu ý", p6=["Phần mềm chỉ cài cho dòng loa được hỗ trợ. Loa khác dòng sẽ được báo và không bị cài gì.","Không tắt loa trong khi đang cài. Nếu rớt mạng, phần mềm tự thử lại; nếu vẫn lỗi, bấm <b>Thử lại</b>.","Cần giúp? Gửi email cho chúng tôi: info@karaokeaihome.com"],
 alt_g="Bước {n} bật Gỡ lỗi USB", alt_app="Phần mềm nâng cấp loa")
T['en'] = dict(
 card_h="Speaker Upgrade for computers", card_p="Install and update the latest Karaoke AI Home software on your speaker over Wi‑Fi, from a Windows PC or a Mac. Always downloads the newest version.",
 win="Download for Windows", mac="Download for macOS", guide="Read the user guide",
 card_steps=["Download the software to your computer and open it.","On the speaker, turn on USB debugging once with the remote (picture guide included).","The software finds the speaker on the same Wi‑Fi. Click <b>Install</b> and wait for <b>Done</b>."],
 g_title="Upgrade your speaker from a computer",
 g_lead="Speaker Upgrade upgrades your speaker to the latest Karaoke AI Home software (6‑language interface, Lambo AI assistant, apps) and keeps it updated, with one click.",
 need="You need: a Windows 10/11 PC or a Mac with macOS 11 or later, an Internet connection, the same Wi‑Fi as the speaker, and the speaker's remote.",
 h1="1. Download and open the software",
 win_h="Windows", win_s=["Click <b>Download for Windows</b> to get <b>KaraokeAIHome-CaiLoa.exe</b>. If the browser asks, choose <b>Keep</b>.","Double‑click the downloaded file.","If you see <b>“Windows protected your PC”</b>: click <b>More info</b> → <b>Run anyway</b>.","The Speaker Upgrade window opens."],
 mac_h="macOS", mac_s=["Click <b>Download for macOS</b> and open the zip to extract <b>KaraokeAIHome-CaiLoa</b>.","Double‑click that file.","If macOS says it can't be opened because it can't be verified: click <b>Done</b>, go to <b>System Settings → Privacy & Security</b>, scroll down, click <b>Open Anyway</b>, then <b>Open</b>.","A Terminal window appears (leave it open while installing) and the software opens in your browser."],
 h2="2. Turn on USB debugging on the speaker (once)", h2_p="Turn the speaker on, connect it to the same Wi‑Fi as the computer, then follow the pictures with the remote. Menus on the speaker may be in Chinese, English or another language; the positions are the same.",
 h3="3. Install", s3=["The software finds the speaker on the network. It appears in the list as <b>Ready</b>: click <b>Install</b>.","The software downloads the newest version, copies it to the speaker and sets it up. The progress bar shows each step.","When it says <b>Done</b>, the speaker restarts and is ready in about a minute."],
 h4="Updating later", p4="When a new version is out, open the software again: speakers with an update show an <b>Update</b> button. The software always downloads the newest version from our server, so you only need to download the software again if it tells you a new version of it exists. Installed speakers can also update themselves with “Update speaker software” in the phone app.",
 h5="Speaker not found?", h6="Good to know", p6=["The software only installs on supported speaker models. Other models are reported and left untouched.","Don't turn the speaker off while installing. If the connection drops the software retries; if it still fails, click <b>Retry</b>.","Need help? Email us: info@karaokeaihome.com"],
 alt_g="Step {n}: turn on USB debugging", alt_app="Speaker Upgrade software")
T['ja'] = dict(
 card_h="パソコン用スピーカーアップグレードツール", card_p="Windows パソコンまたは Mac から、Wi‑Fi 経由でスピーカーに最新の Karaoke AI Home をインストール・更新します。常に最新版をダウンロードします。",
 win="Windows 版をダウンロード", mac="macOS 版をダウンロード", guide="使い方を見る",
 card_steps=["ソフトをパソコンにダウンロードして開きます。","スピーカーでリモコンを使い、USB デバッグを一度だけオンにします（画像ガイド付き）。","同じ Wi‑Fi のスピーカーが自動で見つかります。<b>インストール</b> をクリックし、<b>完了</b> まで待ちます。"],
 g_title="パソコンでスピーカーをアップグレード",
 g_lead="スピーカーアップグレードツールで、スピーカーを最新の Karaoke AI Home（6言語の画面、AIアシスタント Lambo、アプリ）にアップグレードし、その後の更新もワンクリックで行えます。",
 need="必要なもの: Windows 10/11 または macOS 11 以降のパソコン、インターネット、スピーカーと同じ Wi‑Fi、スピーカーのリモコン。",
 h1="1. ソフトをダウンロードして開く",
 win_h="Windows", win_s=["<b>Windows 版をダウンロード</b> をクリックし、<b>KaraokeAIHome-CaiLoa.exe</b> を保存します。ブラウザーに聞かれたら <b>保存</b> を選びます。","ダウンロードしたファイルをダブルクリックします。","<b>「Windows によって PC が保護されました」</b> と出たら、<b>詳細情報</b> → <b>実行</b> をクリックします。","スピーカー設定ツールの画面が開きます。"],
 mac_h="macOS", mac_s=["<b>macOS 版をダウンロード</b> をクリックし、zip を開いて <b>KaraokeAIHome-CaiLoa</b> を取り出します。","そのファイルをダブルクリックします。","「確認できないため開けません」と出たら <b>完了</b> を押し、<b>システム設定 → プライバシーとセキュリティ</b> を下までスクロールして <b>このまま開く</b> → <b>開く</b> をクリックします。","ターミナルが開き（インストール中は閉じないでください）、ブラウザーにソフトの画面が表示されます。"],
 h2="2. スピーカーで USB デバッグをオン（一度だけ）", h2_p="スピーカーの電源を入れてパソコンと同じ Wi‑Fi に接続し、リモコンで画像のとおりに操作します。スピーカーの表示は中国語・英語など他の言語の場合がありますが、項目の位置は同じです。",
 h3="3. インストール", s3=["ネットワーク内のスピーカーが自動で見つかり、<b>準備完了</b> と表示されます。<b>インストール</b> をクリックします。","最新版をサーバーからダウンロードし、スピーカーにコピーして設定します。進行状況バーで各手順がわかります。","<b>完了</b> と出たらスピーカーが再起動し、約 1 分で使えます。"],
 h4="その後の更新", p4="新しい版が出たらソフトをもう一度開きます。更新のあるスピーカーには <b>更新</b> ボタンが出ます。ソフトは常にサーバーから最新版を取得するため、ソフト自体の新しい版が出たと表示されたときだけ再ダウンロードしてください。インストール済みのスピーカーは、スマホアプリの「スピーカーのソフトを更新」でも更新できます。",
 h5="スピーカーが見つからない場合", h6="ご注意", p6=["対応機種にのみインストールします。非対応機種は表示されるだけで、何も変更しません。","インストール中はスピーカーの電源を切らないでください。接続が切れると自動で再試行します。それでも失敗したら <b>再試行</b> をクリックしてください。","お問い合わせ: info@karaokeaihome.com"],
 alt_g="手順 {n}: USB デバッグをオン", alt_app="スピーカーアップグレードツール")
T['ko'] = dict(
 card_h="컴퓨터용 스피커 업그레이드 프로그램", card_p="Windows PC나 Mac에서 Wi‑Fi로 스피커에 최신 Karaoke AI Home 소프트웨어를 설치하고 업데이트합니다. 항상 최신 버전을 내려받습니다.",
 win="Windows용 다운로드", mac="macOS용 다운로드", guide="사용 설명서 보기",
 card_steps=["프로그램을 컴퓨터에 내려받아 엽니다.","스피커에서 리모컨으로 USB 디버깅을 한 번 켭니다(그림 안내 포함).","같은 Wi‑Fi의 스피커를 자동으로 찾습니다. <b>설치</b>를 클릭하고 <b>완료</b>를 기다립니다."],
 g_title="컴퓨터로 스피커 업그레이드하기",
 g_lead="스피커 업그레이드 프로그램으로 스피커를 최신 Karaoke AI Home(6개 언어 화면, AI 비서 Lambo, 앱)으로 업그레이드하고 이후 업데이트도 한 번에 할 수 있습니다.",
 need="필요한 것: Windows 10/11 또는 macOS 11 이상 컴퓨터, 인터넷, 스피커와 같은 Wi‑Fi, 스피커 리모컨.",
 h1="1. 프로그램 내려받고 열기",
 win_h="Windows", win_s=["<b>Windows용 다운로드</b>를 클릭해 <b>KaraokeAIHome-CaiLoa.exe</b>를 받습니다. 브라우저가 물으면 <b>유지</b>를 선택합니다.","받은 파일을 더블클릭합니다.","<b>“Windows의 PC 보호”</b>가 나오면 <b>추가 정보</b> → <b>실행</b>을 클릭합니다.","스피커 설치 프로그램 창이 열립니다."],
 mac_h="macOS", mac_s=["<b>macOS용 다운로드</b>를 클릭하고 zip을 열어 <b>KaraokeAIHome-CaiLoa</b>를 꺼냅니다.","그 파일을 더블클릭합니다.","확인할 수 없어 열 수 없다고 나오면 <b>완료</b>를 누르고 <b>시스템 설정 → 개인정보 보호 및 보안</b>에서 아래로 내려 <b>그래도 열기</b> → <b>열기</b>를 클릭합니다.","터미널 창이 나타나고(설치 중에는 닫지 마세요) 브라우저에 프로그램이 열립니다."],
 h2="2. 스피커에서 USB 디버깅 켜기(한 번만)", h2_p="스피커를 켜고 컴퓨터와 같은 Wi‑Fi에 연결한 뒤 리모컨으로 그림대로 따라 하세요. 스피커 메뉴는 중국어, 영어 등일 수 있지만 위치는 같습니다.",
 h3="3. 설치", s3=["프로그램이 네트워크에서 스피커를 찾아 <b>준비됨</b>으로 표시합니다. <b>설치</b>를 클릭합니다.","서버에서 최신 버전을 받아 스피커에 복사하고 설정합니다. 진행 막대로 단계를 확인할 수 있습니다.","<b>완료</b>가 나오면 스피커가 다시 시작되며 약 1분 후 사용할 수 있습니다."],
 h4="이후 업데이트", p4="새 버전이 나오면 프로그램을 다시 여세요. 업데이트가 있는 스피커에는 <b>업데이트</b> 버튼이 나옵니다. 프로그램은 항상 서버에서 최신 버전을 받으므로, 프로그램 자체의 새 버전이 있다고 알려 줄 때만 다시 내려받으면 됩니다. 설치된 스피커는 휴대폰 앱의 “스피커 소프트웨어 업데이트”로도 업데이트할 수 있습니다.",
 h5="스피커가 보이지 않나요?", h6="알아 두세요", p6=["지원되는 스피커 모델에만 설치합니다. 다른 모델은 알림만 표시하고 아무것도 바꾸지 않습니다.","설치 중에는 스피커를 끄지 마세요. 연결이 끊기면 자동으로 다시 시도하며, 그래도 실패하면 <b>다시 시도</b>를 클릭하세요.","도움이 필요하면 이메일: info@karaokeaihome.com"],
 alt_g="{n}단계: USB 디버깅 켜기", alt_app="스피커 업그레이드 프로그램")
T['fr'] = dict(
 card_h="Outil de mise à niveau pour ordinateur", card_p="Installez et mettez à jour la dernière version du logiciel Karaoke AI Home sur l’enceinte en Wi‑Fi, depuis un PC Windows ou un Mac. Télécharge toujours la version la plus récente.",
 win="Télécharger pour Windows", mac="Télécharger pour macOS", guide="Lire le mode d’emploi",
 card_steps=["Téléchargez le logiciel sur l’ordinateur et ouvrez‑le.","Sur l’enceinte, activez une fois le débogage USB avec la télécommande (guide en images).","Le logiciel trouve l’enceinte sur le même Wi‑Fi. Cliquez sur <b>Installer</b> et attendez <b>Terminé</b>."],
 g_title="Mettre à niveau l’enceinte depuis un ordinateur",
 g_lead="L’outil de mise à niveau installe sur votre enceinte la dernière version de Karaoke AI Home (interface en 6 langues, assistant IA Lambo, applications) et la tient à jour, en un clic.",
 need="Il vous faut : un PC Windows 10/11 ou un Mac sous macOS 11 ou plus récent, Internet, le même Wi‑Fi que l’enceinte et la télécommande de l’enceinte.",
 h1="1. Télécharger et ouvrir le logiciel",
 win_h="Windows", win_s=["Cliquez sur <b>Télécharger pour Windows</b> pour obtenir <b>KaraokeAIHome-CaiLoa.exe</b>. Si le navigateur le demande, choisissez <b>Conserver</b>.","Double‑cliquez sur le fichier téléchargé.","Si « <b>Windows a protégé votre ordinateur</b> » s’affiche : cliquez sur <b>Informations complémentaires</b> → <b>Exécuter quand même</b>.","La fenêtre de l’outil d’installation s’ouvre."],
 mac_h="macOS", mac_s=["Cliquez sur <b>Télécharger pour macOS</b> et ouvrez le zip pour extraire <b>KaraokeAIHome-CaiLoa</b>.","Double‑cliquez sur ce fichier.","Si macOS indique qu’il ne peut pas l’ouvrir faute de vérification : cliquez sur <b>OK</b>, allez dans <b>Réglages Système → Confidentialité et sécurité</b>, descendez, cliquez sur <b>Ouvrir quand même</b>, puis <b>Ouvrir</b>.","Une fenêtre Terminal apparaît (laissez‑la ouverte pendant l’installation) et le logiciel s’ouvre dans le navigateur."],
 h2="2. Activer le débogage USB sur l’enceinte (une seule fois)", h2_p="Allumez l’enceinte, connectez‑la au même Wi‑Fi que l’ordinateur, puis suivez les images avec la télécommande. Les menus de l’enceinte peuvent être en chinois, en anglais ou dans une autre langue ; les positions sont les mêmes.",
 h3="3. Installer", s3=["Le logiciel trouve l’enceinte sur le réseau. Elle apparaît comme <b>Prête</b> : cliquez sur <b>Installer</b>.","Le logiciel télécharge la dernière version, la copie sur l’enceinte et la configure. La barre de progression indique chaque étape.","Quand « <b>Terminé</b> » s’affiche, l’enceinte redémarre et est prête en une minute environ."],
 h4="Mises à jour ensuite", p4="Quand une nouvelle version sort, rouvrez le logiciel : les enceintes concernées affichent un bouton <b>Mettre à jour</b>. Le logiciel télécharge toujours la dernière version depuis notre serveur ; il suffit de le retélécharger s’il vous signale une nouvelle version de lui‑même. Les enceintes déjà installées peuvent aussi se mettre à jour via « Mettre à jour le logiciel de l’enceinte » dans l’app mobile.",
 h5="Enceinte introuvable ?", h6="Bon à savoir", p6=["Le logiciel n’installe que sur les modèles pris en charge. Les autres modèles sont signalés et laissés intacts.","N’éteignez pas l’enceinte pendant l’installation. En cas de coupure, le logiciel réessaie ; si l’échec persiste, cliquez sur <b>Réessayer</b>.","Besoin d’aide ? Écrivez‑nous : info@karaokeaihome.com"],
 alt_g="Étape {n} : activer le débogage USB", alt_app="Outil de mise à niveau")
T['zh'] = dict(
 card_h="电脑版音箱升级工具", card_p="用 Windows 电脑或 Mac，通过 Wi‑Fi 为音箱安装和更新最新的 Karaoke AI Home 软件。始终下载最新版本。",
 win="下载 Windows 版", mac="下载 macOS 版", guide="查看使用说明",
 card_steps=["把软件下载到电脑并打开。","在音箱上用遥控器打开一次 USB 调试（附图解）。","软件会自动找到同一 Wi‑Fi 中的音箱。点击 <b>安装</b>，等待 <b>完成</b>。"],
 g_title="用电脑升级音箱",
 g_lead="音箱升级工具可将音箱升级到最新的 Karaoke AI Home（6 种语言界面、AI 助手 Lambo、应用），之后也能一键更新。",
 need="需要：Windows 10/11 或 macOS 11 及以上的电脑、互联网、与音箱相同的 Wi‑Fi，以及音箱遥控器。",
 h1="1. 下载并打开软件",
 win_h="Windows", win_s=["点击 <b>下载 Windows 版</b>，得到 <b>KaraokeAIHome-CaiLoa.exe</b>。如浏览器询问，选择 <b>保留</b>。","双击下载的文件。","如出现 <b>“Windows 已保护你的电脑”</b>：点击 <b>更多信息</b> → <b>仍要运行</b>。","音箱安装工具窗口打开。"],
 mac_h="macOS", mac_s=["点击 <b>下载 macOS 版</b>，打开 zip 解压出 <b>KaraokeAIHome-CaiLoa</b>。","双击该文件。","如 macOS 提示无法验证而不能打开：点击 <b>完成</b>，进入 <b>系统设置 → 隐私与安全性</b>，向下滚动点击 <b>仍要打开</b>，再点 <b>打开</b>。","会出现一个终端窗口（安装期间请勿关闭），软件在浏览器中打开。"],
 h2="2. 在音箱上打开 USB 调试（只需一次）", h2_p="打开音箱并连接到与电脑相同的 Wi‑Fi，然后用遥控器按图操作。音箱菜单可能是中文、英文或其他语言，位置相同。",
 h3="3. 安装", s3=["软件会在网络中找到音箱，显示 <b>就绪</b>。点击 <b>安装</b>。","软件从服务器下载最新版本，复制到音箱并完成设置。进度条显示每一步。","显示 <b>完成</b> 后，音箱自动重启，约 1 分钟后即可使用。"],
 h4="以后的更新", p4="有新版本时，再次打开软件：有更新的音箱会显示 <b>更新</b> 按钮。软件总是从服务器获取最新版本，只有在提示软件本身有新版本时才需要重新下载。已安装的音箱也可以在手机 App 中用“更新音箱软件”自行更新。",
 h5="找不到音箱？", h6="注意事项", p6=["软件只会安装到支持的音箱型号。其他型号只会提示，不做任何更改。","安装过程中请勿关闭音箱。连接中断时软件会自动重试；仍失败时请点击 <b>重试</b>。","需要帮助？请发邮件：info@karaokeaihome.com"],
 alt_g="第 {n} 步：打开 USB 调试", alt_app="音箱升级工具")

# Nang cap loa va kich hoat bao hanh (khop GUIDES 'upgrade' trong app)
UPG = {'vi': ('Nâng cấp loa và kích hoạt bảo hành', ['Loa còn giao diện tiếng Trung là loa <b>chưa được nâng cấp</b>. Sau khi nâng cấp, loa có đủ 6 ngôn ngữ (Việt, Anh, Nhật, Hàn, Pháp, Trung) và giao diện Karaoke AI Home.', 'Bạn có thể tự nâng cấp bằng điện thoại Android (app Karaoke AI Home → Tài khoản → <b>Nâng cấp loa</b>) hoặc bằng máy tính Windows/Mac theo hướng dẫn trên trang này. iPhone không nâng cấp loa được.', '<b>Kích hoạt bảo hành</b> là việc khác: lần đầu tiên một điện thoại kết nối với loa, loa được kích hoạt bảo hành 12 tháng. Ngày kích hoạt ghi trên máy chủ, không xoá được.', 'Mỗi loa có 5 lượt kết nối điện thoại miễn phí. Mỗi điện thoại mới dùng 1 lượt. Reset gốc loa hay nâng cấp lại cũng không hoàn lượt và không làm lại bảo hành. Gỡ app rồi cài lại trên cùng điện thoại thì không tính lượt mới.', 'Hết lượt thì nâng cấp lên gói VIP để kết nối thêm điện thoại; không bán lượt lẻ.', 'Loa đã nâng cấp rồi thì dùng <b>Cập nhật phần mềm loa</b> (trong app hoặc phần mềm này) để lên bản mới nhất.']), 'en': ('Speaker upgrade and warranty activation', ['A speaker that still shows a Chinese interface has <b>not been upgraded</b>. After the upgrade it has 6 languages (Vietnamese, English, Japanese, Korean, French, Chinese) and the Karaoke AI Home interface.', 'You can upgrade it yourself with an Android phone (Karaoke AI Home app → Account → <b>Upgrade speaker</b>) or with a Windows/Mac computer following this page. iPhones cannot upgrade a speaker.', '<b>Warranty activation</b> is separate: the first time a phone connects to the speaker, its 12‑month warranty is activated. The date is recorded on our server and cannot be reset.', 'Each speaker includes 5 free phone connections. Each new phone uses one. A factory reset or a re‑upgrade does not refund connections or restart the warranty. Uninstalling and reinstalling the app on the same phone does not use a new connection.', 'When the connections run out, upgrade to VIP to connect more phones; single connections are not sold.', 'Once upgraded, use <b>Update speaker software</b> (in the app or this software) to get the newest version.']), 'ja': ('スピーカーのアップグレードと保証の有効化', ['画面が中国語のままのスピーカーは<b>まだアップグレードされていません</b>。アップグレード後は6言語（ベトナム語・英語・日本語・韓国語・フランス語・中国語）と Karaoke AI Home の画面になります。', 'Android スマホ（Karaoke AI Home アプリ → アカウント → <b>スピーカーをアップグレード</b>）か、このページの手順で Windows/Mac パソコンから自分でアップグレードできます。iPhone ではアップグレードできません。', '<b>保証の有効化</b>は別のことです。スマホが初めてスピーカーに接続したとき、12か月保証が有効になります。日付はサーバーに記録され、消せません。', 'スピーカー1台につき無料のスマホ接続が5回あります。新しいスマホごとに1回使います。初期化や再アップグレードをしても回数は戻らず、保証も再開されません。同じスマホでアプリを入れ直しても新たな回数は使いません。', '回数を使い切ったら VIP にアップグレードするとスマホを追加できます。回数のばら売りはありません。', 'アップグレード済みのスピーカーは<b>スピーカーのソフト更新</b>（アプリまたはこのソフト）で最新版にできます。']), 'ko': ('스피커 업그레이드와 보증 활성화', ['화면이 아직 중국어인 스피커는 <b>업그레이드되지 않은</b> 스피커입니다. 업그레이드하면 6개 언어(베트남어, 영어, 일본어, 한국어, 프랑스어, 중국어)와 Karaoke AI Home 화면을 사용합니다.', 'Android 휴대폰(Karaoke AI Home 앱 → 계정 → <b>스피커 업그레이드</b>)이나 이 페이지의 안내대로 Windows/Mac 컴퓨터로 직접 업그레이드할 수 있습니다. iPhone으로는 업그레이드할 수 없습니다.', '<b>보증 활성화</b>는 별개입니다. 휴대폰이 처음 스피커에 연결되면 12개월 보증이 활성화됩니다. 날짜는 서버에 기록되며 지울 수 없습니다.', '스피커마다 무료 휴대폰 연결 5회가 제공됩니다. 새 휴대폰마다 1회를 사용합니다. 초기화나 재업그레이드를 해도 횟수가 돌아오지 않고 보증도 다시 시작되지 않습니다. 같은 휴대폰에서 앱을 지웠다 다시 설치하면 새 횟수를 쓰지 않습니다.', '횟수를 다 쓰면 VIP로 업그레이드해 휴대폰을 더 연결할 수 있으며, 횟수 단품 판매는 없습니다.', '업그레이드된 스피커는 <b>스피커 소프트웨어 업데이트</b>(앱 또는 이 프로그램)로 최신 버전을 받을 수 있습니다.']), 'fr': ('Mise à niveau de l’enceinte et activation de la garantie', ['Une enceinte dont l’interface est encore en chinois <b>n’a pas été mise à niveau</b>. Après la mise à niveau, elle dispose de 6 langues (vietnamien, anglais, japonais, coréen, français, chinois) et de l’interface Karaoke AI Home.', 'Vous pouvez la mettre à niveau vous‑même avec un téléphone Android (app Karaoke AI Home → Compte → <b>Mettre à niveau l’enceinte</b>) ou avec un ordinateur Windows/Mac en suivant cette page. Un iPhone ne peut pas mettre à niveau l’enceinte.', '<b>L’activation de la garantie</b> est distincte : la première fois qu’un téléphone se connecte à l’enceinte, sa garantie de 12 mois est activée. La date est enregistrée sur notre serveur et ne peut pas être effacée.', 'Chaque enceinte inclut 5 connexions de téléphone gratuites. Chaque nouveau téléphone en utilise une. Une réinitialisation ou une nouvelle mise à niveau ne rend pas les connexions et ne relance pas la garantie. Désinstaller puis réinstaller l’app sur le même téléphone ne compte pas comme une nouvelle connexion.', 'Une fois les connexions épuisées, passez à l’offre VIP pour connecter d’autres téléphones ; les connexions ne sont pas vendues à l’unité.', 'Une fois mise à niveau, utilisez <b>Mettre à jour l’enceinte</b> (dans l’app ou ce logiciel) pour obtenir la dernière version.']), 'zh': ('升级音箱与激活保修', ['界面仍是中文的音箱就是<b>尚未升级</b>的音箱。升级后，音箱有 6 种语言（越南语、英语、日语、韩语、法语、中文）和 Karaoke AI Home 界面。', '你可以用 Android 手机（Karaoke AI Home 应用 → 账户 → <b>升级音箱</b>）或按本页说明用 Windows/Mac 电脑自行升级。iPhone 无法升级音箱。', '<b>激活保修</b>是另一回事：手机第一次连接音箱时，音箱的 12 个月保修即被激活。日期记录在服务器上，无法删除。', '每台音箱有 5 次免费手机连接。每部新手机使用 1 次。恢复出厂设置或重新升级都不会退还次数，也不会重新开始保修。在同一部手机上卸载再重装应用不算新的连接。', '次数用完后升级 VIP 即可连接更多手机；不单独出售次数。', '已升级的音箱可用<b>更新音箱软件</b>（在应用或本工具中）获取最新版本。'])}
