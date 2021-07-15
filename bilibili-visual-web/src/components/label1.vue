<template>
  <!-- 
  <h2 id="xxx1">4,332</h2>
  <h6 id="xxx2">+830</h6> -->
  <div>
    <div class="d-flex justify-content-between align-items-center mb-lg">
      <h2 id="xxx1">fuck</h2>
      <i class="la la-arrow-right text-primary la-lg rotate-315" />
    </div>
    <div class="d-flex flex-wrap justify-content-between">
      <div class="mt">
        <h6 id="xxx2">fuck</h6>
        <p class="text-muted mb-0 mr"><small>播放量</small></p>
      </div>
      <div class="mt">
        <h6 id="xxx3">fuck</h6>
        <p class="text-muted mb-0"><small>弹幕量</small></p>
      </div>
      <div class="mt">
        <h6 id="xxx4">fuck</h6>
        <p class="text-muted mb-0 mr"><small>时长</small></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "label1",
  data() {
    return {};
  },
  methods: {
    draw() {
      var elem1 = document.getElementById("xxx1");
      var elem2 = document.getElementById("xxx2");
      var elem3 = document.getElementById("xxx3");
      var elem4 = document.getElementById("xxx4");
      this.$http
        .get("http://131.mollnn.com:5000/api/v/info/BV1144y1q7ve/", {
          headers: { "Access-Control-Allow-Origin": "*" },
        })
        .then((res) => {
          elem1.textContent = res.data[0].view;
          elem2.textContent = res.data[0].view;
          elem3.textContent = res.data[0].danmaku;
          elem4.textContent = res.data[0].duration;
        });
    },
  },
  mounted() {
    this.draw();
  },
};
</script>

<style></style>