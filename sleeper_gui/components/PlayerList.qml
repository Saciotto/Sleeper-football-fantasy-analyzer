pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls

import assets

Item {
    id: root
    property string players
    property alias currentItem: listView.currentItem

    Rectangle {
        anchors.fill:parent
        color: Style.listBackground
        radius: Style.listRadius

        Component {
            id: highlight
            Rectangle {
                width: listView.width
                height: Style.listItemHeight
                color: Style.listItemSelectedBackground
                radius: Style.listItemRadius
                y: listView.currentItem ? listView.currentItem.y : 0
            }
        }

        ScrollView {
            anchors.fill: parent
            ScrollBar.horizontal.policy: ScrollBar.AlwaysOff
            ListView {
                id: listView
                anchors.fill: parent
                anchors.margins: Style.listMargin
                spacing: Style.listSpacing
                clip: true
                model: JSON.parse(root.players)
                delegate: PlayerDelegate {
                    required property int index
                    required property var modelData 
                    width: listView.width
                    height: Style.listItemHeight
                    player: modelData
                    onClicked: listView.currentIndex = index
                }
                focus: true
                highlight: highlight
                highlightFollowsCurrentItem: false
            }
        }
    }
}
