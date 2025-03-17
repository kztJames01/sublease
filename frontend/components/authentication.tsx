'use client';
import React, { useState } from 'react';
import Link from 'next/link';
import { IonIcon } from '@ionic/react';
import axios from 'axios';
import { logoGoogle } from 'ionicons/icons';

const Authentication: React.FC<AuthenticationProps> = ({ type }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [errors, setErrors] = useState<{ [key: string]: string }>({});

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (type === 'signup' && confirmPassword !== password) {
      setErrors({
        confirmPassword: 'Passwords do not match',
      });
      return;
    }

    try {
        const url = type === 'signup' ? '/auth/signup' : '/auth/login';
        const response = await axios.post(url, {
            username,
            email,
            password,
        });
        if (response.status === 201) {
            setErrors({});
            setUsername('');
            setEmail('');
            setPassword('');
            setConfirmPassword('');
            console.log('User created:',response.data);
            alert(type === 'signup' ? 'User created successfully' : 'User logged in successfully');
            if (type === 'signup') {
                window.location.href = '/dashboard';
            }
        }
    } catch (error) {
        if(axios.isAxiosError(error)) {
            setErrors(error.response?.data?.errors);
        }else{
            setErrors({ message: 'Something went wrong' });
        }
    }
  };

  return (
    <div className="flex flex-col w-1/2 my-6 p-6 mx-auto bg-gray-100 rounded-xl font-robo">
      <img src="/logo.png" alt="" className="w-[20vw] my-6" />
      <h1 className="mb-6 text-3xl">{type === 'signup' ? 'Sign Up' : 'Log In'}</h1>
      <form onSubmit={handleSubmit}>
        {type === 'signup' && (
          <div className="mb-3">
            <label className="inline-block mb-2">Email</label><br />
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-2 border rounded"
            />
          </div>
        )}
        <div className="mb-3">
          <label className="inline-block mb-2">Username</label><br />
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        <div className="mb-3">
          <label className="inline-block mb-2">Password</label><br />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-2 border rounded"
          />
        </div>
        {type === 'signup' && (
          <div className="mb-3">
            <label className="inline-block mb-2">Confirm Password</label><br />
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="w-full p-2 border rounded"
            />
          </div>
        )}
        {Object.keys(errors).length > 0 && (
          <div className="mb-3 p-6 bg-red-100 rounded-xl">
            {Object.values(errors).map((error, index) => (
              <p key={index}>{error}</p>
            ))}
          </div>
        )}
        <button type="submit" className="py-4 px-8 text-lg bg-teal-500 hover:bg-teal-700 rounded-xl text-white">
          {type === 'signup' ? 'Sign Up' : 'Log In'}
        </button>
      </form>
      {type === 'signup' ? (
        <Link href="/auth/sign-in" className="mt-6">
          Already have an account? <span className="text-teal-500">Login Here.</span>
        </Link>
      ) : (
        <Link href="/auth/sign-up" className="mt-6 inline-block">
          Create a New Account? <span className="text-teal-500">Sign Up Here.</span>
        </Link>
      )}
      <div className="my-6 h-[1px] w-full bg-black"></div>
      <form action="/api/auth/google" method="POST">
        <button type="submit" className="px-2 py-1 text-gray-700">
          <IonIcon icon={logoGoogle} size="large"></IonIcon>
        </button>
      </form>
    </div>
  );
};

export default Authentication;