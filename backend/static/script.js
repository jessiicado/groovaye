fetch("/get_recommendations")
  .then((response) => response.json())
  .then((data) => {
    const recommendationsList = document.getElementById("recommendations-list");

    data.forEach((item) => {
      const listItem = document.createElement("li");
      listItem.textContent =
        "${item.artist} - #{item.song} (Album: ${item.album})";
      recommendationsList.appendChild(listItem);
    });
  })
  .catch((error) => console.log("Error fetching data:", error));
