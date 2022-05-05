# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.2.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x03P\
i\
mport QtQuick\x0d\x0ai\
mport QtQuick.Wi\
ndow\x0d\x0aimport QtQ\
uick.Controls\x0d\x0a\x0d\
\x0aimport assets 1\
.0\x0d\x0aimport compo\
nents 1.0\x0d\x0a\x0d\x0aWin\
dow {\x0d\x0a    width\
: 640\x0d\x0a    heigh\
t: 480\x0d\x0a    visi\
ble: true\x0d\x0a    t\
itle: qsTr(\x22Slee\
per Football Fan\
tasy Analyzer\x22)\x0d\
\x0a    color: Styl\
e.backgroundColo\
r\x0d\x0a\x0d\x0a    Compone\
nt.onCompleted: \
function() {\x0d\x0a  \
      masterCont\
roller.navigatio\
nController.goDa\
shboardView();\x0d\x0a\
    }\x0d\x0a\x0d\x0a    Nav\
igationBar {\x0d\x0a  \
      id: naviga\
tionBar\x0d\x0a       \
 anchors {\x0d\x0a    \
        top: par\
ent.top\x0d\x0a       \
     bottom: par\
ent.bottom\x0d\x0a    \
        left: pa\
rent.left\x0d\x0a     \
   }\x0d\x0a    }\x0d\x0a\x0d\x0a \
   StackView {\x0d\x0a\
        id: cont\
entFrame\x0d\x0a      \
  anchors {\x0d\x0a   \
         top: pa\
rent.top\x0d\x0a      \
      bottom: pa\
rent.bottom\x0d\x0a   \
         right: \
parent.right\x0d\x0a  \
          left: \
navigationBar.ri\
ght\x0d\x0a        }\x0d\x0a\
        initialI\
tem: \x22qrc:/views\
/LoginView.qml\x22\x0d\
\x0a        clip: t\
rue\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x05m\
i\
mport QtQuick\x0d\x0ai\
mport QtQuick.Co\
ntrols\x0d\x0aimport Q\
tQuick.Layouts\x0d\x0a\
\x0d\x0aimport assets \
1.0\x0d\x0a\x0d\x0aItem {\x0d\x0a \
   Rectangle {\x0d\x0a\
        anchors.\
fill: parent\x0d\x0a  \
      color: Sty\
le.backgroundCol\
or\x0d\x0a\x0d\x0a        Co\
lumnLayout {\x0d\x0a  \
          anchor\
s.fill: parent\x0d\x0a\
            spac\
ing: 20\x0d\x0a\x0d\x0a     \
       Item {\x0d\x0a \
               L\
ayout.fillHeight\
: true\x0d\x0a        \
    }\x0d\x0a\x0d\x0a       \
     Label {\x0d\x0a  \
              te\
xt: qsTr(\x22Login\x22\
)\x0d\x0a             \
   font.pixelSiz\
e: 50\x0d\x0a         \
       Layout.al\
ignment: Qt.Alig\
nCenter\x0d\x0a       \
     }\x0d\x0a\x0d\x0a      \
      TextField \
{\x0d\x0a             \
   placeholderTe\
xt: qsTr(\x22Userna\
me\x22)\x0d\x0a          \
      horizontal\
Alignment: TextI\
nput.AlignHCente\
r\x0d\x0a             \
   Layout.alignm\
ent: Qt.AlignCen\
ter\x0d\x0a           \
     Layout.fill\
Width: true\x0d\x0a   \
             Lay\
out.maximumWidth\
: 0.75 * parent.\
width\x0d\x0a         \
   }\x0d\x0a\x0d\x0a        \
    Button {\x0d\x0a  \
              id\
: button\x0d\x0a      \
          backgr\
ound: Rectangle \
{\x0d\x0a             \
       implicitW\
idth: 100\x0d\x0a     \
               i\
mplicitHeight: 4\
0\x0d\x0a             \
       color: bu\
tton.down ? \x22#00\
ceb8\x22 : \x22#00ceb8\
\x22\x0d\x0a             \
       border.co\
lor: \x22#26282a\x22\x0d\x0a\
                \
    border.width\
: 1\x0d\x0a           \
         radius:\
 height / 2\x0d\x0a   \
             }\x0d\x0a\
                \
text: qsTr(\x22Cont\
inue\x22)\x0d\x0a        \
        Layout.a\
lignment: Qt.Ali\
gnCenter\x0d\x0a      \
      }\x0d\x0a\x0d\x0a     \
       Item {\x0d\x0a \
               L\
ayout.fillHeight\
: true\x0d\x0a        \
    }\x0d\x0a        }\
\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x00\xde\
i\
mport QtQuick\x0d\x0ai\
mport QtQuick.Co\
ntrols\x0d\x0a\x0d\x0aimport\
 assets 1.0\x0d\x0a\x0d\x0aI\
tem {\x0d\x0a    Recta\
ngle {\x0d\x0a        \
anchors.fill: pa\
rent\x0d\x0a        co\
lor: Style.backg\
roundColor\x0d\x0a\x0d\x0a  \
      Button {\x0d\x0a\
            text\
: \x22Ok\x22\x0d\x0a        \
}\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x00\xf0\
i\
mport QtQuick\x0d\x0a\x0d\
\x0aimport assets 1\
.0\x0d\x0a\x0d\x0aItem {\x0d\x0a  \
  Rectangle {\x0d\x0a \
       anchors.f\
ill: parent\x0d\x0a   \
     color: Styl\
e.backgroundColo\
r\x0d\x0a\x0d\x0a        Tex\
t {\x0d\x0a           \
 anchors.centerI\
n: parent\x0d\x0a     \
       text: \x22Te\
am View\x22\x0d\x0a      \
  }\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x00\xf5\
i\
mport QtQuick\x0d\x0a\x0d\
\x0aimport assets 1\
.0\x0d\x0a\x0d\x0aItem {\x0d\x0a  \
  Rectangle {\x0d\x0a \
       anchors.f\
ill: parent\x0d\x0a   \
     color: Styl\
e.backgroundColo\
r\x0d\x0a\x0d\x0a        Tex\
t {\x0d\x0a           \
 anchors.centerI\
n: parent\x0d\x0a     \
       text: \x22Da\
shboard View\x22\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x05\
\x00|\xfc\xe3\
\x00v\
\x00i\x00e\x00w\x00s\
\x00\x0e\
\x0e\x9f\xcf\x5c\
\x00M\
\x00a\x00s\x00t\x00e\x00r\x00V\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
\x00\x0d\
\x09vR\xfc\
\x00L\
\x00o\x00g\x00i\x00n\x00V\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
\x00\x12\
\x0de{\x1c\
\x00B\
\x00e\x00s\x00t\x00L\x00i\x00n\x00e\x00u\x00p\x00V\x00i\x00e\x00w\x00.\x00q\x00m\
\x00l\
\x00\x0c\
\x04\xa1U\xbc\
\x00T\
\x00e\x00a\x00m\x00V\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
\x00\x11\
\x0cUd\x1c\
\x00D\
\x00a\x00s\x00h\x00b\x00o\x00a\x00r\x00d\x00V\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00|\x00\x00\x00\x00\x00\x01\x00\x00\x09\xa7\
\x00\x00\x01\x80\x8c\x90\xdd\xf3\
\x00\x00\x002\x00\x00\x00\x00\x00\x01\x00\x00\x03T\
\x00\x00\x01\x80\x8c\xb24<\
\x00\x00\x00\x9a\x00\x00\x00\x00\x00\x01\x00\x00\x0a\x9b\
\x00\x00\x01\x80\x8c\x17\xdc\xaa\
\x00\x00\x00R\x00\x00\x00\x00\x00\x01\x00\x00\x08\xc5\
\x00\x00\x01\x80\x8c\x1e\xf2\xb1\
\x00\x00\x00\x10\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x80\x8c\x16Wt\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
