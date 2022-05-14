import QtQuick
import QtQuick.Controls

import assets 1.0

ItemDelegate {
    property var player
    signal itemClicked

    id: root
    width: parent != null ? parent.width : 0
    implicitHeight: playerPosition.height + 4

    Rectangle {
        id: playerPosition
        anchors {
            left: parent.left
            verticalCenter: parent.verticalCenter
        }
        width: 45
        height: 30
        color: {
            switch (player.fantasy_positions[0]) {
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
        radius: 5
        Label {
            anchors.fill: parent
            text: player.fantasy_positions[0]
            horizontalAlignment: Label.AlignHCenter
            verticalAlignment: Label.AlignVCenter
            font {
                pixelSize: 16
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
        text: player.full_name
        font {
            pixelSize: 16
        }
    }
}
