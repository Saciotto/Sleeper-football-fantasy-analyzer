import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import assets 1.0

Item {
    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor

        ColumnLayout {
            anchors.fill: parent
            spacing: 20

            Item {
                Layout.fillHeight: true
            }

            Label {
                text: qsTr("Login")
                font.pixelSize: 50
                Layout.alignment: Qt.AlignCenter
            }

            TextField {
                placeholderText: qsTr("Username")
                horizontalAlignment: TextInput.AlignHCenter
                Layout.alignment: Qt.AlignCenter
                Layout.fillWidth: true
                Layout.maximumWidth: 0.75 * parent.width
            }

            Button {
                id: button
                background: Rectangle {
                    implicitWidth: 100
                    implicitHeight: 40
                    color: button.down ? "#00ceb8" : "#00ceb8"
                    border.color: "#26282a"
                    border.width: 1
                    radius: height / 2
                }
                text: qsTr("Continue")
                Layout.alignment: Qt.AlignCenter
            }

            Item {
                Layout.fillHeight: true
            }
        }
    }
}
