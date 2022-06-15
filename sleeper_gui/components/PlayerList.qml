import QtQuick
import QtQuick.Controls

import assets 1.0

Item {
    id: root
    property string players
    property alias currentItem: list.currentItem

    Rectangle {
        anchors.fill:parent
        color: Style.listBackground
        radius: Style.listRadius

        Component {
            id: highlight
            Rectangle {
                width: list.width
                height: Style.listItemHeight
                color: Style.listItemSelectedBackground
                radius: Style.listItemRadius
                y: list.currentItem ? list.currentItem.y : 0
            }
        }

        ScrollView {
            anchors.fill: parent
            ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
            ListView {
                id: list
                anchors.fill: parent
                anchors.margins: Style.listMargin
                spacing: Style.listSpacing
                clip: true
                model: JSON.parse(root.players)
                delegate: PlayerDelegate {
                    width: list.width
                    height: Style.listItemHeight
                    player: modelData
                    onClicked: list.currentIndex = index
                }
                focus: true
                highlight: highlight
                highlightFollowsCurrentItem: false
            }
        }
    }
}