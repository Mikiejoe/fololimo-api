
import mongoose from "mongoose";
import { Region, City, SubCounty } from "../models/Location.js";
const PROVINCE_DATA = {
  Central: {
    Kiambu: [
      "Gatundu North",
      "Gatundu South",
      "Githunguri",
      "Juja",
      "Kabete",
      "Kiambaa",
      "Kiambu Town",
      "Kikuyu",
      "Limuru",
      "Lari",
      "Ruiru",
      "Thika Town",
    ],
    "Murang'a": [
      "Gatanga",
      "Kahuro",
      "Kandara",
      "Kangema",
      "Kigumo",
      "Kiharu",
      "Mathioya",
      "Murang'a South",
    ],
    Nyeri: [
      "Kieni East",
      "Kieni West",
      "Mathira East",
      "Mathira West",
      "Mukureini",
      "Nyeri Central",
      "Tetu",
      "Othaya",
    ],
    Kirinyaga: [
      "Kirinyaga Central",
      "Kirinyaga East",
      "Kirinyaga West",
      "Mwea East",
      "Mwea West",
    ],
    Nyandarua: ["Kinangop", "Kipipiri", "Ndaragwa", "Ol Kalou", "Ol Joro Orok"],
  },
  "Rift Valley": {
    Nakuru: [
      "Bahati",
      "Gilgil",
      "Kuresoi North",
      "Kuresoi South",
      "Molo",
      "Naivasha",
      "Nakuru East",
      "Nakuru West",
      "Njoro",
      "Rongai",
      "Subukia",
    ],
    "Uasin Gishu": ["Ainabkoi", "Kapsaret", "Kesses", "Moiben", "Soy", "Turbo"],
    Kericho: [
      "Ainamoi",
      "Belgut",
      "Bureti",
      "Kipkelion East",
      "Kipkelion West",
      "Soin/Sigowet",
    ],
    Baringo: [
      "Baringo Central",
      "Baringo North",
      "Baringo South",
      "Eldama Ravine",
      "Mogotio",
      "Tiaty",
    ],
    Narok: [
      "Narok East",
      "Narok North",
      "Narok South",
      "Narok West",
      "Trans Mara East",
      "Trans Mara West",
    ],
    Bomet: ["Bomet Central", "Bomet East", "Chepalungu", "Konoin", "Sotik"],
    "Elgeyo-Marakwet": [
      "Keiyo North",
      "Keiyo South",
      "Marakwet East",
      "Marakwet West",
    ],
    Kajiado: [
      "Kajiado Central",
      "Kajiado East",
      "Kajiado North",
      "Kajiado South",
      "Kajiado West",
    ],
    Laikipia: ["Laikipia East", "Laikipia North", "Laikipia West"],
    Nandi: ["Aldai", "Chesumei", "Emgwen", "Mosop", "Nandi Hills", "Tinderet"],
    Samburu: ["Samburu Central", "Samburu East", "Samburu North"],
    "Trans Nzoia": ["Cherangany", "Endebess", "Kwanza", "Saboti", "Kiminini"],
    Turkana: [
      "Loima",
      "Turkana Central",
      "Turkana East",
      "Turkana North",
      "Turkana South",
      "Turkana West",
    ],
    "West Pokot": ["Kapenguria", "Kipkomo", "Pokot South", "Sigor"],
  },
  Eastern: {
    Embu: ["Manyatta", "Mbeere North", "Mbeere South", "Runyenjes"],
    Kitui: [
      "Kitui Central",
      "Kitui East",
      "Kitui Rural",
      "Kitui South",
      "Kitui West",
      "Mwingi Central",
      "Mwingi North",
      "Mwingi West",
    ],
    Machakos: [
      "Kangundo",
      "Kathiani",
      "Machakos Town",
      "Masinga",
      "Matungulu",
      "Mavoko",
      "Mwala",
      "Yatta",
    ],
    Makueni: ["Kaiti", "Kibwezi East", "Kibwezi West", "Kilome", "Makueni"],
    Marsabit: ["Laisamis", "Moyale", "North Horr", "Saku"],
    Meru: [
      "Buuri",
      "Central Imenti",
      "Igembe Central",
      "Igembe North",
      "Igembe South",
      "North Imenti",
      "South Imenti",
      "Tigania East",
      "Tigania West",
    ],
    "Tharaka-Nithi": ["Chuka/Igambang'ombe", "Maara", "Tharaka"],
    Isiolo: ["Isiolo North", "Isiolo South"],
  },
  Nyanza: {
    "Homa Bay": [
      "Homa Bay Town",
      "Kabondo Kasipul",
      "Kasipul",
      "Karachuonyo",
      "Mbita",
      "Ndhiwa",
      "Rangwe",
      "Suba",
    ],
    Kisii: [
      "Bomachoge Borabu",
      "Bomachoge Chache",
      "Bobasi",
      "Kitutu Chache North",
      "Kitutu Chache South",
      "Nyaribari Chache",
      "Nyaribari Masaba",
      "South Mugirango",
    ],
    Kisumu: [
      "Kisumu Central",
      "Kisumu East",
      "Kisumu West",
      "Muhoroni",
      "Nyakach",
      "Nyando",
      "Seme",
    ],
    Migori: [
      "Awendo",
      "Kuria East",
      "Kuria West",
      "Nyatike",
      "Rongo",
      "Suna East",
      "Suna West",
      "Uriri",
    ],
    Nyamira: [
      "Borabu",
      "Manga",
      "Masaba North",
      "Nyamira North",
      "Nyamira South",
    ],
    Siaya: ["Alego Usonga", "Bondo", "Gem", "Rarieda", "Ugenya", "Ugunja"],
  },
  Western: {
    Bungoma: [
      "Bumula",
      "Kabuchai",
      "Kanduyi",
      "Kimilili",
      "Mt Elgon",
      "Sirisia",
      "Tongaren",
      "Webuye East",
      "Webuye West",
    ],
    Busia: [
      "Butula",
      "Funyula",
      "Matayos",
      "Nambale",
      "Teso North",
      "Teso South",
    ],
    Kakamega: [
      "Butere",
      "Khwisero",
      "Lugari",
      "Lurambi",
      "Malava",
      "Mumias East",
      "Mumias West",
      "Navakholo",
      "Shinyalu",
      "Ikolomani",
    ],
    Vihiga: ["Emuhaya", "Hamisi", "Luanda", "Sabatia", "Vihiga"],
  },
  Coast: {
    Kilifi: [
      "Ganze",
      "Kaloleni",
      "Kilifi North",
      "Kilifi South",
      "Magarini",
      "Malindi",
      "Rabai",
    ],
    Kwale: ["Kinango", "Lunga Lunga", "Matuga", "Msambweni"],
    Lamu: ["Lamu East", "Lamu West"],
    Mombasa: ["Changamwe", "Jomvu", "Kisauni", "Likoni", "Mvita", "Nyali"],
    "Taita-Taveta": ["Mwatate", "Taveta", "Voi", "Wundanyi"],
    "Tana River": ["Bura", "Galole", "Garsen"],
  },
  "North Eastern": {
    Garissa: [
      "Balambala",
      "Dadaab",
      "Fafi",
      "Garissa Township",
      "Ijara",
      "Lagdera",
    ],
    Mandera: [
      "Banissa",
      "Lafey",
      "Mandera East",
      "Mandera North",
      "Mandera South",
      "Mandera West",
    ],
    Wajir: [
      "Eldas",
      "Tarbaj",
      "Wajir East",
      "Wajir North",
      "Wajir South",
      "Wajir West",
    ],
  },
  Nairobi: {
    Nairobi: [
      "Dagoretti North",
      "Dagoretti South",
      "Embakasi Central",
      "Embakasi East",
      "Embakasi North",
      "Embakasi South",
      "Embakasi West",
      "Kamukunji",
      "Kasarani",
      "Kibra",
      "Lang'ata",
      "Makadara",
      "Mathare",
      "Ruaraka",
      "Starehe",
      "Westlands",
    ],
  },
};



const connectDB = async () => {
  try {
    await mongoose.connect("mongodb://localhost:27017/fololimo", {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("✅ MongoDB Connected");
  } catch (error) {
    console.error("❌ MongoDB connection error:", error);
    process.exit(1);
  }
};

const populateProvincesCountiesAndSubCounties = async () => {
  try {
    await connectDB();

    for (const [provinceName, counties] of Object.entries(PROVINCE_DATA)) {
      let province = await Region.findOneAndUpdate(
        { region: provinceName },
        { region: provinceName },
        { upsert: true, new: true }
      );
      console.log(`✅ Created/Found province: ${provinceName}`);

      for (const [countyName, subCounties] of Object.entries(counties)) {
        let county = await City.findOneAndUpdate(
          { city: countyName, region: province._id },
          { city: countyName, region: province._id },
          { upsert: true, new: true }
        );
        console.log(`✅ Created/Found county: ${countyName} in province: ${provinceName}`);

        for (const subCountyName of subCounties) {
          await SubCounty.findOneAndUpdate(
            { sub_county: subCountyName, city: county._id },
            { sub_county: subCountyName, city: county._id },
            { upsert: true, new: true }
          );
          console.log(`✅ Created/Found sub-county: ${subCountyName} in county: ${countyName}`);
        }
      }
    }

    console.log("🎉 Data population complete!");
    mongoose.disconnect();
  } catch (error) {
    console.error("❌ Error populating data:", error);
    mongoose.disconnect();
  }
};

populateProvincesCountiesAndSubCounties();


