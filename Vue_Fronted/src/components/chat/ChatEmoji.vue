<template>
    <div class="emoji-Bigbox">
      <el-scrollbar ref="emojiScroll" class="emojiScroll">
        <div
            class="emoji-box"
            v-for="(item, index) in emoji_icon"
            :key="index"
            @click="pickEmoji(index)"
        >
          {{ item }}
        </div>
      </el-scrollbar>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        emoji_icon: [
          "😀",
          "😃",
          "😄",
          "😁",
          "😆",
          "😅",
          "🤣",
          "😂",
          "🙂",
          "🙃",
          "😉",
          "😊",
          "😇",
          "😍",
          "🤩",
          "😘",
          "😗",
          "😚",
          "😙",
          "😋",
          "😛",
          "😜",
          "🤪",
          "😝",
          "🤑",
          "🤗",
          "🤭",
          "🤫",
          "🤔",
          "🤐",
          "🤨",
          "😐",
          "😑",
          "😶",
          "😏",
          "😒",
          "🙄",
          "😬",
          "🤥",
          "😌",
          "😔",
          "😪",
          "🤤",
          "😴",
          "😷",
          "🤒",
          "🤕",
          "🤢",
          "🤮",
          "🤧",
          "😵",
          "🤯",
          "🤠",
          "😎",
          "🤓",
          "🧐",
          "😕",
          "😟",
          "🙁",
          "😮",
          "😯",
          "😲",
          "😳",
          "😦",
          "😧",
          "😨",
          "😰",
          "😥",
          "😢",
          "😭",
          "😱",
          "😖",
          "😣",
          "😞",
          "😓",
          "😩",
          "😫",
          "😤",
          "😡",
          "😠",
          "🤬",
          "😈",
          "👿",
          "💀",
          "💩",
          "🤡",
          "👹",
          "👺",
          "👻",
          "👽",
          "👾",
          "🤖",
          "😺",
          "😸",
          "😹",
          "😻",
          "😼",
          "😽",
          "🙀",
          "😿",
          "😾",
          "💋",
          "👋",
          "🤚",
          "🖐",
          "✋",
          "🖖",
          "👌",
          "🤞",
          "🤟",
          "🤘",
          "🤙",
          "👈",
          "👉",
          "👆",
          "🖕",
          "👇",
          "👍",
          "👎",
          "✊",
          "👊",
          "🤛",
          "🤜",
          "👏",
          "🙌",
          "👐",
          "🤲",
          "🤝",
          "🙏",
          "💅",
          "🤳",
          "💪",
          "👂",
          "👃",
          "🧠",
          "👀",
          "👁",
          "👅",
          "👄",
          "👶",
          "🧒",
          "👦",
          "👧",
          "🧑",
          "👱",
          "👨",
          "🧔",
          "👱‍",
          "👨‍",
          "👨‍",
          "👨‍",
          "👨‍",
          "👩",
          "👱‍",
          "👩‍",
          "👩‍",
          "👩‍",
          "👩‍",
          "🧓",
          "👴",
          "👵",
          "🙍",
          "🙍‍",
          "🙍‍",
          "🙎",
          "🙎‍",
          "🙎‍",
          "🙅",
          "🙅‍",
          "🙅‍",
          "🙆",
          "🙆‍",
          "🙆‍",
          "💁",
          "💁‍",
          "💁‍",
          "🙋",
          "🙋‍",
          "🙋‍",
          "🙇",
          "🙇‍",
          "🙇‍",
          "🤦",
          "🤦‍",
          "🤦‍",
          "🤷",
          "🤷‍",
          "🤷‍",
          "👨‍⚕️",
          "👩‍⚕️",
          "👨‍🎓",
          "👩‍🎓",
          "👨‍🏫",
          "👩‍🏫",
          "👨‍⚖️",
          "👩‍⚖️",
          "👨‍🌾",
          "👩‍🌾",
          "👨‍🍳",
          "👩‍🍳",
          "👨‍🔧",
          "👩‍🔧",
          "👨‍🏭",
          "👩‍🏭",
          "👨‍💼",
          "👩‍💼",
          "👨‍🔬",
          "👩‍🔬",
          "👨‍💻",
          "👩‍💻",
          "👨‍🎤",
          "👩‍🎤",
          "👨‍🎨",
          "👩‍🎨",
          "👨‍✈️",
          "👩‍✈️",
          "👨‍🚀",
          "👩‍🚀",
          "👨‍🚒",
          "👩‍🚒",
          "👮",
          "👮‍♂️",
          "👮‍♀️",
          "🕵",
          "🕵️‍♂️",
          "🕵️‍♀️",
          "💂",
          "💂‍",
          "💂‍",
          "👷",
          "👷‍",
          "👷‍",
          "🤴",
          "👸",
          "👳",
          "👳‍",
          "👳‍",
          "👲",
          "🧕",
          "🤵",
          "👰",
          "🤰",
          "🤱",
          "👼",
          "🎅",
          "🤶",
          "🧙",
          "🧙‍",
          "🧙‍",
          "🧚",
          "🧚‍",
          "🧚‍",
          "🧛",
          "🧛‍",
          "🧛‍",
          "🧜",
          "🧜‍",
          "🧜‍",
          "🧝",
          "🧝‍",
          "🧝‍",
          "🧞",
          "🧞‍",
          "🧞‍",
          "🧟",
          "🧟‍",
          "🧟‍",
          "💆",
          "💆‍",
          "💆‍",
          "💇",
          "💇‍",
          "💇‍",
          "🚶",
          "🚶‍",
          "🚶‍",
          "🏃",
          "🏃‍",
          "🏃‍",
          "💃",
          "🕺",
          "🕴",
          "👯",
          "👯‍",
          "👯‍",
          "🧖",
          "🧖‍",
          "🧖‍",
          "🧘",
          "👭",
          "👫",
          "👬",
          "💏",
          "👨‍",
          "👩‍",
          "💑",
          "👨‍",
          "👩‍",
          "👪",
          "👨‍👩‍👦",
          "👨‍👩‍👧",
          "👨‍👩‍👧‍👦",
          "👨‍👩‍👦‍👦",
          "👨‍👩‍👧‍👧",
          "👨‍👨‍👦",
          "👨‍👨‍👧",
          "👨‍👨‍👧‍👦",
          "👨‍👨‍👦‍👦",
          "👨‍👨‍👧‍👧",
          "👩‍👩‍👦",
          "👩‍👩‍👧",
          "👩‍👩‍👧‍👦",
          "👩‍👩‍👦‍👦",
          "👩‍👩‍👧‍👧",
          "👨‍👦",
          "👨‍👦‍👦",
          "👨‍👧",
          "👨‍👧‍👦",
          "👨‍👧‍👧",
          "👩‍👦",
          "👩‍👦‍👦",
          "👩‍👧",
          "👩‍👧‍👦",
          "👩‍👧‍👧",
          "🗣",
          "👤",
          "👥",
          "👣",
          "🌂",
          "☂",
          "👓",
          "🕶",
          "👔",
          "👕",
          "👖",
          "🧣",
          "🧤",
          "🧥",
          "🧦",
          "👗",
          "👘",
          "👙",
          "👚",
          "👛",
          "👜",
          "👝",
          "🎒",
          "👞",
          "👟",
          "👠",
          "👡",
          "👢",
          "👑",
          "👒",
          "🎩",
          "🎓",
          "🧢",
          "⛑",
          "💄",
          "💍",
          "💼"
        ]
      }
    },
    methods: {
      pickEmoji(idx) {
        return this.$emit("selectEmoji", this.emoji_icon[idx])
      },
    }
  }
  </script>
  <style scoped>
  
  .emoji-Bigbox {
    height: 300px;
    background: #fff;
    border-radius: 10px;
  }
  
  .emoji-Bigbox .el-scrollbar  .el-scrollbar__wrap /deep/{
    overflow-y: hidden !important;
  }
  
  .emoji-Bigbox .emojiScroll{
    height: 310px;
  }
  
  .emoji-Bigbox .emoji-box{
    display: inline-block;
    width: 30px;
    height: 30px;
    font-size: 22px;
    text-align: center;
    transition: all 0.3s;
    cursor: pointer;
  }
  
  
  
  </style>
  