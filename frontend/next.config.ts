import type { NextConfig } from "next";
import path from "path";
const nextConfig: NextConfig = {
  reactStrictMode: true,
  webpack: (config, { isServer }) => {
    config.resolve.alias['@'] = path.resolve(__dirname);
    if (!isServer) {
      
      config.module.rules.push({
        test: /\.entry\.js$/,
        use: {
          loader: "file-loader",
          options: {
            name: "[name].[ext]",
            outputPath: "static/stencil/",
            publicPath: "/_next/static/stencil/",
          },
        },
      });
    }
    return config;
  },
};

export default nextConfig;