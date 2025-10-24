# 1️⃣ Imagen base
FROM node:18

# 2️⃣ Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3️⃣ Copiar archivos de dependencias
COPY package*.json ./

# 4️⃣ Instalar dependencias
RUN npm install

# 5️⃣ Copiar todo el código fuente al contenedor
COPY . .

# 6️⃣ Exponer puerto de la aplicación
EXPOSE 3000

# 7️⃣ Comando para ejecutar la app
CMD ["node", "app.js"]
