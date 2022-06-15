import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import assets 1.0

Item {
/*
    Connections {
        target: masterController.loginController
        function onLoggedChanged() {
            masterController.navigationController.goDashboardView()
        }
        function onLoginFailed() {
            busyIndicator.visible = false;
            button.visible = true;
        }
    }
    */
    Rectangle {
        anchors.fill:parent
        color: Style.backgroundColor

        Label {
            id: label
            text: qsTr("Last Update") + '\n' + masterController.dashboardController.lastUpdate()
            width: parent.width * 0.8
            anchors {
                left: parent.left
                right: parent.right
                bottom: parent.verticalCenter
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
                top: label.bottom
                horizontalCenter: parent.horizontalCenter
                topMargin: 20
            }
            Button {
                id: button
                text: qsTr("Update")
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
                    masterController.dashboardController.update()
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
