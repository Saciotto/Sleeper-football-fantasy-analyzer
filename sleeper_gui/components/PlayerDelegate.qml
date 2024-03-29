import QtQuick
import QtQuick.Controls

import assets

ItemDelegate {
    property var player
    signal itemClicked

    id: item

    Rectangle {
        id: playerPosition
        anchors {
            left: parent.left
            leftMargin: Style.listItemInternalMargin
            verticalCenter: parent.verticalCenter
        }
        width: Style.playerPositionBoxWidth
        height: Style.playerPositionBoxHeight
        color: {
            switch (item.player.fantasy_positions[0]) {
            case 'QB':
                return Style.qbBackgroundColor;
            case 'RB':
                return Style.rbBackgroundColor;
            case 'WR':
                return Style.wrBackgroundColor;
            case 'TE':
                return Style.teBackgroundColor;
            case 'DL':
                return Style.dlBackgroundColor;
            case 'LB':
                return Style.lbBackgroundColor;
            case 'DB':
                return Style.dbBackgroundColor;
            }
            return Style.genericBackgroundColor;
        }
        radius: Style.listItemRadius
        Label {
            anchors.fill: parent
            text: item.player.fantasy_positions[0]
            horizontalAlignment: Label.AlignHCenter
            verticalAlignment: Label.AlignVCenter
            font {
                pixelSize: Style.playerTextFontSize
                bold: true
            }
        }
    }
    Label {
        anchors {
            left: playerPosition.right
            leftMargin: 8
            verticalCenter: parent.verticalCenter
        }
        text: item.player.full_name
        font {
            pixelSize: Style.playerTextFontSize
        }
    }
}
