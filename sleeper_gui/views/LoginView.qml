import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import assets 1.0

Item {

    Connections {
        target: app.loginController
        function onLoggedChanged() {
            app.navigationController.goDashboardView()
        }
        function onLoginFailed() {
            busyIndicator.visible = false;
            button.visible = true;
        }
    }
    Rectangle {
        anchors.fill:parent
        color: Style.backgroundColor

        TextField {
            id: username
            width: parent.width * 0.8
            anchors {
                left: parent.left
                right: parent.right
                centerIn: parent
            }
            horizontalAlignment: Label.AlignHCenter
            placeholderText: qsTr("Username")
            font.pixelSize: 16
        }
        Label {
            text: qsTr("Enter your Sleeper username")
            width: parent.width * 0.8
            anchors {
                bottom: username.top
                horizontalCenter: parent.horizontalCenter
                bottomMargin: 20
            }
            horizontalAlignment: Label.AlignHCenter
            wrapMode: Label.WordWrap
            font.pixelSize: 32
            Layout.alignment: Qt.AlignCenter
        }
        Item {
            height: button.height
            width: button.width
            anchors {
                top: username.bottom
                horizontalCenter: parent.horizontalCenter
                topMargin: 20
            }
            Button {
                id: button
                text: qsTr("Continue")
                background: Rectangle {
                    implicitWidth: 120
                    implicitHeight: 50
                    color: button.down ? "#00ceb8" : "#00ceb8"
                    border.color: "#26282a"
                    border.width: 1
                    radius: height / 2
                }
                font.pixelSize: 16
                anchors.centerIn: parent
                onClicked: {
                    button.visible = false;
                    busyIndicator.visible = true;
                    app.loginController.login(username.text)
                }
            }
            BusyIndicator {
                id: busyIndicator
                height: button.height
                anchors.centerIn: parent
                visible: false
                running: true
            }
        }
    }
}
