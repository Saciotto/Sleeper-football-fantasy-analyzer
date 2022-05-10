import QtQuick
import QtQuick.Controls

import assets 1.0

Item {
    id: root
    property string players

    ListView {
        anchors.fill: parent
        model: JSON.parse(root.players)
        delegate: PlayerDelegate {
            player: modelData
        }
    }
}