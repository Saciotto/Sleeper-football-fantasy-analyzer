import QtQuick
import QtQuick.Controls

import assets 1.0
import components 1.0

Item {

    Connections {
        target: masterController.teamController
        function onUsersChanged() {
            usersBox.currentIndex = usersBox.indexOfValue(masterController.teamController.username);
        }
    }

    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor

        ComboBox {
            id: leagueBox
            model: masterController.teamController.leagues
            onActivated: masterController.teamController.league = currentValue
            anchors {
                left: parent.left
                right: parent.horizontalCenter
                top: parent.top
                margins: 4
            }
            Component.onCompleted: currentIndex = indexOfValue(masterController.teamController.league)
        }

        ComboBox {
            id: usersBox
            model: masterController.teamController.users
            onActivated: masterController.teamController.username = currentValue
            anchors {
                left: leagueBox.right
                right: parent.right
                top: parent.top
                margins: 4
            }
            Component.onCompleted: currentIndex = indexOfValue(masterController.teamController.username)
        }

        PlayerList {
            anchors {
                left: parent.left
                top: leagueBox.bottom
                bottom: parent.bottom
                margins: 8
            }
            width: 0.5 * parent.width
            clip: true
            players: masterController.teamController.players
        }

    }
}
