import QtQuick

import assets 1.0

import QtQuick.Controls.Material

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
                return contentFrame.replace("../views/DashboardView.qml");
            } else {
                return contentFrame.replace("../views/LoginView.qml");
            }
        }
        function onGoTeamView() {
            selectedView = navbar.teamView;
            return contentFrame.replace("../views/TeamView.qml");
        }
        function onGoBestLineupView() {
            selectedView = navbar.bestLineupView;
            return contentFrame.replace("../views/BestLineupView.qml");
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
