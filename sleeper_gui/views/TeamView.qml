import QtQuick
import QtQuick.Controls

import assets 1.0
import components 1.0

Item {

    Connections {
        target: app.team
        function onLeagueUsersChanged() {
            usersBox.currentIndex = usersBox.indexOfValue(app.team.selectedUser);
        }
    }

    Rectangle {
        anchors.fill: parent
        color: Style.backgroundColor

        ComboBox {
            id: leagueBox
            model: app.team.leagues
            onActivated: app.team.selectedLeague = currentValue
            anchors {
                left: parent.left
                right: parent.horizontalCenter
                top: parent.top
                margins: 8
            }
            Component.onCompleted: currentIndex = indexOfValue(app.team.selectedLeague)
        }

        ComboBox {
            id: usersBox
            model: app.team.leagueUsers
            onActivated: app.team.selectedUser = currentValue
            anchors {
                left: leagueBox.right
                right: parent.right
                top: parent.top
                margins: 8
            }
            Component.onCompleted: currentIndex = indexOfValue(app.team.selectedUser)
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
            players: app.team.players
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
                text: JSON.stringify(JSON.parse(app.team.playerStatistics(playerList.currentItem.player.player_id)),null,2)
            }
        }
    }
}
