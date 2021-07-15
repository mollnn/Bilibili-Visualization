<template>
  <div class="table-responsive">
    <table class="table table-striped table-lg mb-0 requests-table">
      <thead>
        <tr class="text-muted">
          <th>视频id</th>
          <th>up id</th>
          <th>是否转载</th>
          <th>分区</th>
          <th>播放</th>
          <th>投币</th>
          <th>评论</th>
          <th>点赞</th>
          <th>收藏</th>
        </tr>
      </thead>
      <tbody>
        <td id = "xxx8"></td>
        <td id = "xxx9"></td>
        <td id = "xxx10"></td>
        <td id = "xxx11"></td>
        <td id = "xxx12"></td>
        <td id = "xxx13"></td>
        <td id = "xxx14"></td>
        <td id = "xxx15"></td>
        <td id = "xxx16"></td>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "label4",
  data() {
    return {};
  },
  methods: {
    draw() {
      var elem1 = document.getElementById("xxx8");
      var elem2 = document.getElementById("xxx9");
      var elem3 = document.getElementById("xxx10");
      var elem4 = document.getElementById("xxx11");
      var elem5 = document.getElementById("xxx12");
      var elem6 = document.getElementById("xxx13");
      var elem7 = document.getElementById("xxx14");
      var elem8 = document.getElementById("xxx15");
      var elem9 = document.getElementById("xxx16");
      this.$http
        .get("http://131.mollnn.com:5000/api/v/info/BV1144y1q7ve/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
          elem1.textContent = res.data[0].bvid;
          elem2.textContent = res.data[0].aid;
          elem3.textContent = res.data[0].iscopy;
          elem4.textContent = res.data[0].tname;
          elem5.textContent = res.data[0].view;
          elem6.textContent = res.data[0].coin;
          elem7.textContent = res.data[0].reply;
          elem8.textContent = res.data[0].likes;
          elem9.textContent = res.data[0].favorite;
        });
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style></style>