import QtQuick
import QtQuick.Controls

import assets 1.0

Item {
    id: root
    property string players

    Rectangle {
        anchors.fill:parent
        color: "#293142"
        radius: 8

        Component {
            id: highlight
            Rectangle {
                width: list.width; height: 40
                color: "lightsteelblue"; radius: 5
                y: list.currentItem.y
            }
        }

        ListView {
            id: list
            anchors.fill: parent
            anchors.margins: 8
            spacing: 8
            clip: true
            model: JSON.parse(root.players)
            delegate: PlayerDelegate {
                player: modelData
                onClicked: list.currentIndex = index
            }
            focus: true
            highlight: highlight
            highlightFollowsCurrentItem: false
            ScrollIndicator.vertical: ScrollIndicator { }
        }
    }
}