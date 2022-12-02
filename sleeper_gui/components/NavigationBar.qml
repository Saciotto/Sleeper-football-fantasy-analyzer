import QtQuick

import assets 1.0

Item {
    id: navbar
    property string selectedView: ""

    readonly property string dashboardView: "DashboardView"
    readonly property string bestLineupView: "BestLineupView"
    readonly property string teamView: "LoginView"

    Connections {
        target: masterController.navigationController
        function onGoDashboardView() {
            selectedView = navbar.dashboardView;
            if (masterController.loginController.logged) {
                return contentFrame.replace("qrc:/views/DashboardView.qml");
            } else {
                return contentFrame.replace("qrc:/views/LoginView.qml");
            }
        }
        function onGoTeamView() {
            selectedView = navbar.teamView;
            return contentFrame.replace("qrc:/views/TeamView.qml");
        }
        function onGoBestLineupView() {
            selectedView = navbar.bestLineupView;
            return contentFrame.replace("qrc:/views/BestLineupView.qml");
        }
    }

    width: Style.navigationBarWidth

    Rectangle {
        anchors.fill: parent
        color: Style.navigationBarColor
        Column {
            width: parent.width
            NavigationButton {
                iconCharacter: "\ue871"
                description: qsTr("Dashboard")
                selected: navbar.selectedView === navbar.dashboardView
                onNavigationButtonClicked: {
                    masterController.navigationController.goDashboardView();
                }
            }
            NavigationButton {
                iconCharacter: "\ue7ef"
                description: qsTr("Team")
                selected: navbar.selectedView === navbar.teamView
                enabled: masterController.loginController.logged
                onNavigationButtonClicked: {
                    masterController.navigationController.goTeamView();
                }
            }
            NavigationButton {
                iconCharacter: "\ue838"
                description: qsTr("Best Lineup")
                selected: navbar.selectedView === navbar.bestLineupView
                enabled: masterController.loginController.logged
                onNavigationButtonClicked: {
                    masterController.navigationController.goBestLineupView();
                }
            }
        }
    }
}
