import QtQuick
import QtQuick.Controls

import assets 1.0
import components 1.0

Item {

    Connections {
        target: app.teamController
        function onLeagueUsersChanged() {
            usersBox.currentIndex = usersBox.indexOfValue(app.teamController.selectedUser);
        }
    }

    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor

        ComboBox {
            id: leagueBox
            model: app.teamController.leagues
            onActivated: app.teamController.selectedLeague = currentValue
            anchors {
                left: parent.left
                right: parent.horizontalCenter
                top: parent.top
                margins: 8
            }
            Component.onCompleted: currentIndex = indexOfValue(app.teamController.selectedLeague)
        }

        ComboBox {
            id: usersBox
            model: app.teamController.leagueUsers
            onActivated: app.teamController.selectedUser = currentValue
            anchors {
                left: leagueBox.right
                right: parent.right
                top: parent.top
                margins: 8
            }
            Component.onCompleted: currentIndex = indexOfValue(app.teamController.selectedUser)
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
            players: app.teamController.players
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
                text: JSON.stringify(JSON.parse(app.teamController.playerStatistics(playerList.currentItem.player.player_id)),null,2)
            }
        }
    }
}
