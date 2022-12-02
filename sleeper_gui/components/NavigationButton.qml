import QtQuick
import QtQuick.Controls

import assets

Item {
    id: navbutton

    property alias iconCharacter: iconCharacter.text
    property alias description: description.text
    property bool selected: false

    signal navigationButtonClicked()

    width: Style.navigationBarWidth
    height: Style.navigationButtonHeight

    Rectangle {
        id: background
        anchors.fill: parent
        color: navbutton.selected ? Style.navigationButtonPressedColor : Style.navigationButtonColor

        Rectangle {
            id: selectionIndicator
            width: 4
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            color: Style.navigationButtonSelectionIndicatorColor
            visible: navbutton.selected
        }

        Column {
            spacing: Style.navigationButtonSpacing
            anchors.centerIn: parent
            Label {
                id: iconCharacter
                width: background.width
                text: "\ue000"
                font {
                    family: Style.fontMaterialIcons
                    pixelSize: Style.navigationButtonIconPixSize
                }
                horizontalAlignment: Text.AlignHCenter
            }
            Label {
                id: description
                width: background.width
                font.pixelSize: Style.navigationButtonTextPixSize
                text: "SET ME!!"
                horizontalAlignment: Text.AlignHCenter
            }
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            cursorShape: Qt.PointingHandCursor
            enabled: parent.enabled && !navbutton.selected
            hoverEnabled: parent.enabled && !navbutton.selected
            onEntered: background.state = "hover";
            onExited: background.state = ""
            onClicked: navbutton.navigationButtonClicked()
        }

        states: [
            State {
                name: "hover"
                PropertyChanges {
                    target: background
                    color: Style.navigationButtonHoveredColor
                }
            }
        ]
    }
}
