import QtQuick
import QtQuick.Controls

import assets 1.0
import components 1.0

Item {

    Connections {
        target: masterController.teamController
        function onLeagueUsersChanged() {
            usersBox.currentIndex = usersBox.indexOfValue(masterController.teamController.selectedUser);
        }
    }

    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor

        ComboBox {
            id: leagueBox
            model: masterController.teamController.leagues
            onActivated: masterController.teamController.selectedLeague = currentValue
            anchors {
                left: parent.left
                right: parent.horizontalCenter
                top: parent.top
                margins: 8
            }
            Component.onCompleted: currentIndex = indexOfValue(masterController.teamController.selectedLeague)
        }

        ComboBox {
            id: usersBox
            model: masterController.teamController.leagueUsers
            onActivated: masterController.teamController.selectedUser = currentValue
            anchors {
                left: leagueBox.right
                right: parent.right
                top: parent.top
                margins: 8
            }
            Component.onCompleted: currentIndex = indexOfValue(masterController.teamController.selectedUser)
        }

        PlayerList {
            id: playerList
            anchors {
                left: parent.left
                right: parent.horizontalCenter
                top: leagueBox.bottom
                bottom: parent.bottom
                margins: 8
            }
            clip: true
            players: masterController.teamController.players
        }

        ScrollView {
            anchors {
                left: parent.horizontalCenter
                right: parent.right
                top: leagueBox.bottom
                bottom: parent.bottom
                margins: 8
            }
            Label {
                anchors.fill: parent
                text: JSON.stringify(JSON.parse(masterController.teamController.playerStatistics(playerList.currentItem.player.player_id)),null,2)
            }
        }


    }
}
