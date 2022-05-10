import QtQuick
import QtQuick.Controls

import assets 1.0

Item {
    property var player

    id: root
    implicitHeight: playerPosition.height + 4
    Rectangle {
        id: playerPosition
        anchors {
            left: parent.left
            verticalCenter: parent.verticalCenter
        }
        width: 30
        height: 20
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
        }
    }
    Label {
        anchors {
            left: playerPosition.right
            leftMargin: 4
            verticalCenter: parent.verticalCenter
        }
        text: player.full_name
    }
}
