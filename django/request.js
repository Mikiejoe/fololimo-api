async function postFarm() {
  let bodyContent = JSON.stringify({
    name: "My Farm",
    location: "Chepalungu",
    size: 23.54,
  });
  let headersList = {
    Authorization: `Token  ${token}`,
    "Content-Type": "application/json",
  };

  let response = await fetch(
    "https://fololimo-api-eight.vercel.app/api/v1/insights/farms/",
    {
      method: "POST",
      body: bodyContent,
      headers: headersList,
    }
  );
  console.log(response);

//   let data = await response.text();
//   console.log(data);
}

postFarm();
