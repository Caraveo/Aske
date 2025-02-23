class NextjsModel:
    """Model for generating Next.js project structure and files"""

    @staticmethod
    def get_model_prompt_component():
        """Generate ModelPrompt component"""
        return '''"use client";

import { useState } from 'react';

interface ModelPromptProps {
  onSubmit: (input: string) => void;
}

const ModelPrompt: React.FC<ModelPromptProps> = ({ onSubmit }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    onSubmit(input.trim());
    setInput('');
  };

  return (
    <div style={{ margin: '2rem 0' }}>
      <h2>Model Prompt</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter your prompt..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={{ padding: '0.5rem', width: '300px', marginRight: '1rem' }}
        />
        <button type="submit" style={{ padding: '0.5rem 1rem' }}>
          Submit
        </button>
      </form>
    </div>
  );
};

export default ModelPrompt;
'''

    @staticmethod
    def get_index_page():
        """Generate index page with ModelPrompt"""
        return '''"use client";

import ModelPrompt from '../components/ModelPrompt';

export default function Home() {
  const handlePromptSubmit = (input: string) => {
    console.log('User input:', input);
    // Add logic to process the prompt input
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Welcome to My Next.js App</h1>
      <p>This project is set up with best practices in mind.</p>
      <ModelPrompt onSubmit={handlePromptSubmit} />
    </div>
  );
}
''' 