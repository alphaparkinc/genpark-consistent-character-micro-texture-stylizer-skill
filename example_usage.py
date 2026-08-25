from client import ConsistentCharacterMicroTextureStylizerClient

def main():
    client = ConsistentCharacterMicroTextureStylizerClient()
    res = client.generate_consistent_styled_character(88129, 'Space commander inspecting orbital docking bay', 'CINEMATIC_V6_MICRO_TEXTURE')
    print('Character Job: ' + res['character_job_id'] + ' (Seed: ' + str(res['seed_identity']) + ')')
    print('Facial Consistency: ' + str(res['facial_consistency_similarity_pct']) + '% | Resolution: ' + res['skin_micro_texture_resolution'])
    print('Lighting Fidelity: ' + str(res['lighting_ray_tracing_fidelity_score']) + '% | LoRA Export: ' + str(res['lora_embedding_exported']))
    print('Image URL: ' + res['generated_character_image_url'])

if __name__ == '__main__':
    main()
