import QtQuick

import assets 1.0

Item {
    property string selectedView: ""

    readonly property string dashboardView: "DashboardView"
    readonly property string bestLineupView: "BestLineupView"
    readonly property string teamView: "LoginView"

    Connections {
        target: masterController.navigationController
        function onGoDashboardView() {
            selectedView = dashboardView;
            if (masterController.loginController.logged) {
                return contentFrame.replace("qrc:/views/DashboardView.qml");
            } else {
                return contentFrame.replace("qrc:/views/LoginView.qml");
            }
        }
        function onGoTeamView() {
            selectedView = teamView;
            return contentFrame.replace("qrc:/views/TeamView.qml");
        }
        function onGoBestLineupView() {
            selectedView = bestLineupView;
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
                selected: selectedView === dashboardView
                onNavigationButtonClicked: {
                    masterController.navigationController.goDashboardView();
                }
            }
            NavigationButton {
                iconCharacter: "\ue7ef"
                description: qsTr("Team")
                selected: selectedView === teamView
                enabled: masterController.loginController.logged
                onNavigationButtonClicked: {
                    masterController.navigationController.goTeamView();
                }
            }
            NavigationButton {
                iconCharacter: "\ue838"
                description: qsTr("Best Lineup")
                selected: selectedView === bestLineupView
                enabled: masterController.loginController.logged
                onNavigationButtonClicked: {
                    masterController.navigationController.goBestLineupView();
                }
            }
        }
    }
}
